from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from direct_todo.models import *
from taggit.models import *
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    return render_to_response("index.html",{},
                              context_instance=RequestContext(request))

@login_required
def profile(request):
    user=request.user
    search = request.GET.get("search")
    order = request.GET.get("orderby")
    due = request.GET.get("due")
    
    if not order:
        order = "due_date"    
    
    if due:
        due_dt = datetime.strptime(due,"%m/%d/%Y")
      
    if search and due:
        tasks = Task.objects.get(
            Q(title__contains=search)|Q(tags__name__contains=search),
            user=user).filter(due_date=due_dt).order_by(order)
        search = "%s, Due: %s" % (search,due)
    elif search:
        tasks = Task.objects.filter(
            Q(title__contains=search)|Q(tags__name__contains=search),
            user=user).order_by(order)    
    elif due:
        tasks = Task.objects.filter(user=user).filter(
            due_date=due_dt).order_by(order)
        search = "Due: "+due
    else:
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
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponse("true")


@login_required
def add_task(request):
    task_title = request.GET.get('title')
    task_date = datetime.strptime(request.GET.get('date'),"%m/%d/%Y")
    task_tags = request.GET.get('tags')
    new_task = Task(title=task_title,due_date=task_date,user=request.user)
    new_task.save()
    for tag in task_tags.split(","):
        new_task.tags.add(tag)
    new_task.save()
    return HttpResponse(new_task.id)


@login_required
def get_task(request,task_id):
    task = Task.objects.get(id=task_id)
    ctx = {"task":task}
    return render_to_response("single_task.html",ctx,
                              context_instance=RequestContext(request))


@login_required
def filter_by_tag(request,tag=""):
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
