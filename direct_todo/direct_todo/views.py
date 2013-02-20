from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from direct_todo.models import *
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def home(request):
    return render_to_response("index.html",{},
                              context_instance=RequestContext(request))

@login_required
def profile(request):
    user=request.user
    tasks = Task.objects.filter(user=user)
    ctx= {
        "user":user,
        "tasks":tasks
    }
    return render_to_response("profile.html",ctx,
                              context_instance=RequestContext(request))
    
def delete_task(request,task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponse("true")

def add_task(request):
    task_title = request.GET.get('title')
    task_date = datetime.strptime(request.GET.get('date'),"%m/%d/%Y")
    task_tags = request.GET.get('tags')
    new_task = Task(title=task_title,due_date=task_date,user=request.user)
    new_task.save()
    #need to split by commas for propper adding
    for tag in task_tags.split(","):
        print tag
        new_task.tags.add(tag)
    new_task.save()
    #task.delete()
    return HttpResponse(new_task.id)

#def get_task(request,task_id):
#    document.get
