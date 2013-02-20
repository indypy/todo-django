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
    
