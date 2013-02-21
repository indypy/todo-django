from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'direct_todo.views.home', name='home'),
    # url(r'^direct_todo/', include('direct_todo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'direct_todo.views.home'),
    url(r'login/', 
        'django.contrib.auth.views.login', 
        {'template_name': 'index.html'}
        ),
    url(r'logout/', 
        'django.contrib.auth.views.logout', 
        {'template_name': 'index.html'}
        ),    
    url(r'^profile/tags/$', 
        'direct_todo.views.filter_by_tag'),
    
    url(r'^profile/tags/(?P<tag>.+)/$', 
        'direct_todo.views.filter_by_tag'),
    
    url(r'^profile/add-task/$', 
        'direct_todo.views.add_task'),
    url(r'^profile/get-task/(?P<task_id>\w+)/$', 
        'direct_todo.views.get_task'),
    url(r'^profile/delete-task/(?P<task_id>\w+)/$', 
        'direct_todo.views.delete_task'),
    
    
    url(r'^profile/$', 'direct_todo.views.profile'),    
    url(r'^admin/', include(admin.site.urls)),    
)

