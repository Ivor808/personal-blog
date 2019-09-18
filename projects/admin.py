from django.contrib import admin
from projects.models import Project
from django.db import models
from pagedown.widgets import AdminPagedownWidget


class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


admin.site.register(Project, ProjectAdmin)
