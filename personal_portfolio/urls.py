
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("projects/", include("projects.urls")),
    path("aboutme/", include("aboutme.urls")),
    path("blog/", include("blog.urls")),
    path("", include("projects.urls"))
]
