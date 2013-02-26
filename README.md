#Todo-Django
A django web app for basic task lists that are segmented by user.

##Setup Instructions 
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

###Includes many features inherited from Django:
  - Robust Admin
  - Supports multiple databases
  - Robust templating engine

## Third Party Code
- [DirectEmployers UI Framework](https://github.com/DirectEmployers/UI-Framework) (based on Bootstrap)
- [Django-Taggit](https://github.com/alex/django-taggit)

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
