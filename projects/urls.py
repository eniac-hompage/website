from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("<int:pk>/", views.ProjectDetail.as_view(), name="detail"),
    path("<int:pk>/edit", views.EditProjectView.as_view(), name="edit"),
    path("/creates", views.CreateProjectView.as_view(), name="create"),
 
    path('<int:pk>/delete', views.DeleteProjectView.as_view(), name='delete'),
]