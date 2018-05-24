from django.urls import path

from . import views


app_name = "courses"
urlpatterns = [
    path("", views.CourseListView.as_view(), name='list'),
    path("courses/<int:pk>/", views.CourseDetailView.as_view(), name="detail"),
#    path("courses/<int:course_pk>/<int:step_pk>/", views.step_detail, name='step'),
    path("courses/<int:course_pk>/<int:step_pk>/", views.StepDetailView.as_view(), name='step'),
]