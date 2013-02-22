from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from todo_django.models import *

from taggit.models import *

def home(request):
    """
    Handles the root view
    
    Inputs:
    :request:   Django request object
    
    Returns:
    django render_to_response object
    
    """
    return render_to_response("index.html",{},
                              context_instance=RequestContext(request))

@login_required
def profile(request):
    """
    View that handles the primary task view page.
    
    Inputs:
    :request:   Django request object
    
    Optional Get Arguments:
    :search:    search string used to look for matches in the title or tags
    :orderby:   the field to order by
    :due:       a date to match during searches
    
    Returns:
    django render_to_response object
    
    """
    user=request.user
    search = request.GET.get("search")
    order = request.GET.get("orderby")
    due = request.GET.get("due")
    
    if not order: #set the default order to ascending date"
        order = "due_date"    
    
    if due: #convert the date to a datetime object
        due_dt = datetime.strptime(due,"%m/%d/%Y")
      
    if search and due: #search by phrase and filter by date
        tasks = Task.objects.get(
            Q(title__contains=search)|Q(tags__name__contains=search),
            user=user).filter(due_date=due_dt).order_by(order)
        search = "%s, Due: %s" % (search,due)
    elif search: #search by phrase
        tasks = Task.objects.filter(
            Q(title__contains=search)|Q(tags__name__contains=search),
            user=user).order_by(order)    
    elif due: #filter by date
        tasks = Task.objects.filter(user=user).filter(
            due_date=due_dt).order_by(order)
        search = "Due: "+due
    else: #default to listing everything
        tasks = Task.objects.filter(user=user).order_by(order)
        
    ctx= {
        "user":user,
        "tasks":tasks,
        "search":search
    }
    return render_to_response("profile.html",ctx,
                              context_instance=RequestContext(request))


@login_required
def delete_task(request,task_id):
    """
    Deletes a task from the system. This view is designed to be called by AJAX.
    For the purposes of this demo, we assume it will always work.
    
    Inputs:
    :request:   django request object
    :task_id:   integer value of the task id
    
    Returns:
    true
    """
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponse("true")


@login_required
def add_task(request):
    """
    Adds a task to the system. This is a view intended to be called by AJAX.
    
    Inputs:
    :request:   django request object
    
    Returns:
    :new_task.id:   The integer id of the new task
    
    """
    task_title = request.GET.get('title')
    task_date = datetime.strptime(request.GET.get('date'),"%m/%d/%Y")
    task_tags = request.GET.get('tags')
    new_task = Task(title=task_title,due_date=task_date,user=request.user)
    new_task.save()
    for tag in task_tags.split(","): # add each tag
        new_task.tags.add(tag)
    new_task.save()
    return HttpResponse(new_task.id)


@login_required
def get_task(request,task_id):
    """
    Gets a task from the system. This view is intended to be called by AJAX.
    
    Inputs:
    :request:   django request object
    :task_id:   the integer id of the task to retrieve
    
    Returns:
    django render_to_response of a table row.
    """
    task = Task.objects.get(id=task_id)
    ctx = {"task":task}
    if task:
        return render_to_response("single_task.html",ctx,
                                  context_instance=RequestContext(request))
    else:
        return HttpResponse("false")


@login_required
def filter_by_tag(request,tag=""):
    """
    Used to display a list of tags independent of tasks. It does not filter 
    based on the user.
    
    Inputs:
    :request:   django request object
    :tag:       the string value of the tag to filter for. If empty, all tags
                are returned.
    
    Returns:
    render_to_reponse rendered template
    
    """
    user=request.user
    ctx= {
        "user":user,
    }
    template = "view_tags.html"
    if tag:
        tasks = Task.objects.filter(tags__name__in=[tag])
        ctx["tasks"] = tasks
        ctx["search"] = "tag: "+tag
        template = "profile.html"
    else:
        tags = Tag.objects.order_by('name')
        ctx["tags"] = tags
    
    return render_to_response(template,ctx,
                              context_instance=RequestContext(request))
