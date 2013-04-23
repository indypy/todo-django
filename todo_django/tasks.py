from jobtastic import JobtasticTask

class ExportTasksAsCsv(JobtasticTask):
    """
    Create a CSV file with all of the tasks.
    """
    significant_kwargs = [('task_pks', str)]
    herd_avoidance_timeout = 120  # Give it two minutes
    # Cache for 10 minutes if they haven't added any todos
    cache_duration = 600

    def calculate_result(self, task_pks):
        return {}

