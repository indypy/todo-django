from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo_django.views.home', name='home'),
    # url(r'^todo_django/', include('todo_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'todo_django.views.home'),
    url(r'login/', 
        'django.contrib.auth.views.login', 
        {'template_name': 'index.html'}
        ),
    url(r'logout/', 
        'django.contrib.auth.views.logout', 
        {'template_name': 'index.html'}
        ),    
    url(r'^profile/tags/$', 
        'todo_django.views.filter_by_tag'),
    
    url(r'^profile/tags/(?P<tag>.+)/$', 
        'todo_django.views.filter_by_tag'),
    
    url(r'^profile/add-task/$', 
        'todo_django.views.add_task'),
    url(r'^profile/get-task/(?P<task_id>\w+)/$', 
        'todo_django.views.get_task'),
    url(r'^profile/delete-task/(?P<task_id>\w+)/$', 
        'todo_django.views.delete_task'),
    
    
    url(r'^profile/$', 'todo_django.views.profile'),    
    url(r'^admin/', include(admin.site.urls)),    
)

