from django.urls import include, path

from . import views

urlpatterns = [
    path('projects/' ,views.ProjectsView) ,
    path('contact/' ,views.ContactView) ,
]