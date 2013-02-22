from django.contrib import admin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from models import Task 

class TagTaskFilter(admin.SimpleListFilter):
    title = ('Tags')

    parameter_name = 'id'

    def lookups(self, request, model_admin):
        user_tasks = model_admin.queryset(request)
        return Task.tags.filter(task__in=user_tasks).values_list('slug', 'name')

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset
        return queryset.filter(tags__slug=self.value())

class TaskAdmin(admin.ModelAdmin):
    list_filter = (TagTaskFilter,) 
    fields = ('title', 'tags', 'due_date')
    search_fields = ['title', 'tags']

    date_hierarchy = 'due_date'

    def queryset(self, request):
        qs = super(TaskAdmin, self).queryset(request)
        user = getattr(request, 'user', None)
        if user.is_superuser:
            return qs.all() 
        return qs.filter(user=user)

    def has_delete_permission(self, request, obj=None):
        user = getattr(request, 'user', None)
        if not user.is_superuser and not user == getattr(obj, 'user', user):
            return False
        return super(TaskAdmin, self).has_delete_permission(request, obj)

    def has_change_permission(self, request, obj=None):
        user = getattr(request, 'user', None)
        if not user.is_superuser and not user == getattr(obj, 'user', user):
            return False
        return super(TaskAdmin, self).has_delete_permission(request, obj)

    def save_model(self, request, obj, form, change):
        try:
            obj.user
        except ObjectDoesNotExist:
            obj.user = request.user
        obj.save()


admin.site.register(Task, TaskAdmin)
