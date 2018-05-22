from django.urls import path

from . import views


urlpatterns = [
    path("", views.CourseListView.as_view(), name='list')
]