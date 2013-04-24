import csv
import cStringIO
import codecs
import time

from django.conf import settings

from jobtastic import JobtasticTask

from todo_django.models import Task


class ExportTasksAsCsv(JobtasticTask):
    """
    Create a CSV file with all of the tasks.
    """
    significant_kwargs = [('task_pks', str)]
    herd_avoidance_timeout = 120  # Give it two minutes
    # Cache for 10 minutes if they haven't added any todos
    cache_duration = 600

    def calculate_result(self, task_pks):
        tasks = Task.objects.filter(pk__in=task_pks)
        num_tasks = len(task_pks)

        # Let folks know we started
        self.update_progress(0, num_tasks)

        # Gather all of the data for our CSV
        task_data = []
        for counter, task in enumerate(tasks):
            task_data.append([
                task.pk, task.title, task.due_date.isoformat(),
            ])

            # Normally, we'd use an update_frequency of a couple hundred to
            # avoid hitting the cache so often when it will only be read every
            # couple seconds. For demo purposes though, let's wear it out!
            self.update_progress(counter, num_tasks, update_frequency=1)
            if getattr(settings, 'TODO_EXPORT_VERY_SLOWLY', False):
                time.sleep(5)

        # Now convert the data to CSV format
        w = CSVWriter()

        # Build the header row
        header = ['id', 'title', 'due_date']
        w.writerow(header)

        # Now add each task's data
        w.writerows(task_data)

        # Encode the results as UTF16 for Excel's sake
        csv_data = unicode(w.getvalue(), 'utf16')

        return {'data': csv_data}


class UnicodeWriter(object):
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


class CSVWriter(UnicodeWriter):
    def __init__(self):
        self.buffer = cStringIO.StringIO()
        super(CSVWriter, self).__init__(self.buffer, delimiter='\t')

    def writerow(self, row):
        return super(CSVWriter, self).writerow([unicode(s) for s in row])

    def getvalue(self):
        csv_data = self.buffer.getvalue()
        # Microsoft excel does not recognize UTF-8 encoding
        # when opening csv files. Re-encode as UTF-16.
        csv_data = csv_data.decode('utf8').encode('utf16')
        return csv_data

