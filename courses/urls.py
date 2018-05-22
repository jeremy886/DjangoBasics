from django.urls import path

from . import views


urlpatterns = [
    path("", views.CourseListView.as_view(), name='list'),
    path("courses/<int:pk>/", views.CourseDetailView.as_view(), name="detail"),
]