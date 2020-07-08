# Todo-Django
A django web app for basic task lists that are segmented by user.

## Setup Instructions
Todo-Django was developed on Ubuntu 12, but any Linux environment with python 2.6+ should work.
- *It is recommended you use a virtual environment*
- $ pip install -r requirements.txt
- $ python manage.py syncdb
- $ python manage.py runserver

## Features
- Requires Login
  - Users must be created via Django Admin
- Create Task
- Delete Task
- Tag Tasks
  - Also provides filtering by tag name
- Search Tasks
  - search by date
  - search by title
  - search by tag name
- Single UI for most important tasks
  - creation, search, and deleting of tasks is all AJAX

### Includes many features inherited from Django:
  - Robust Admin
  - Supports multiple databases
  - Robust templating engine

## Third Party Code
- [DirectEmployers UI Framework](https://github.com/DirectEmployers/UI-Framework) (based on Bootstrap)
- [Django-Taggit](https://github.com/alex/django-taggit)

## Enhancements

### Celery CSV report

You now have the ability to download a CSV of all of your tasks!
The CSV is generated in the background using
[Celery](http://www.celeryproject.org/).
We're also using [Jobtastic](http://policystat.github.io/jobtastic/)
on the python side to add easy progress reporting and caching.
On the client side, we're using
[jquery-celery](https://github.com/PolicyStat/jquery-celery)
to provide a Bootstrap progress bar for friendly reporting of the CSV progress.

#### Installation

Install [Celery](http://www.celeryproject.org/)
and [Jobtastic](http://policystat.github.io/jobtastic/),
then build the database tables required by Django-Celery.

    $ pip install -r requirements.txt
    $ python manage.py syncdb

You'll also need to run a celery worker.

    $ python manage.py celery worker


-----------------------------
# IndyPy Web Framework Shootout

[IndyPy](http://www.meetup.com/python-182/) is having  a web framework shootout to compare several popular python based web frameworks. The goal is to see how the frameworks compare from a developer perspective.

## ToDo app details

Create an app using the following specifications:

- Login is required to be able to use the app
- Add a todo list item
- Todo list item consists of
  - Title
  - Tags
  - Due date
- Edit a todo list item
- Complete a todo list item (delete)
- View list of todo items
- Sort list of todo items based on date by default
- Ability to sort list by title
- View listing of todo items by tag

This will show off the following features: CRUD, MVC, authentication, authorization and data storage.

## Frameworks

- Bottle
- Django
- Flask
- Pyramid

Any other frameworks want to represent?

## Future Shootouts

In future installments, the apps could be given more features such as:

- Batching
- Configuration panel
- Expose an API
- iCal feed
- Lists
- Location / context
- Notes
- Priorities
- Recurrence
- Search
- Sharing
- Time estimation
- Time zone handling
