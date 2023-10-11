from django.contrib import admin
from .models import Project
from .models import ProjectInstance

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ('title', 'company', 'date_published')
    list_display = ('id', 'title', 'company', 'date_published')
@admin.register(ProjectInstance)
class ProjectInstanceAdmin(admin.ModelAdmin):
    list_filter = ('id','project', 'date_acquired', 'date_of_end_contract', 'investment', 'investor')
    list_display = ('id', 'project', 'date_acquired', 'date_of_end_contract', 'investment', 'investor')
