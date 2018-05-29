from django.urls import path, re_path

from . import views


app_name = "courses"
urlpatterns = [
    path("", views.CourseListView.as_view(), name="list"),
    path("<int:pk>/", views.CourseDetailView.as_view(), name="detail"),
    path("<int:course_pk>/t<int:step_pk>/", views.TextDetailView.as_view(), name="text"),
    path("<int:course_pk>/q<int:step_pk>/", views.QuizDetailView.as_view(), name="quiz"),
    path("<int:course_pk>/create_quiz/", views.QuizCreateView.as_view(), name="create_quiz"),
    path("<int:course_pk>/edit_quiz/<int:quiz_pk>/", views.QuizEditView.as_view(), name="edit_quiz"),
    path("<int:course_pk>/edit_text/<int:text_pk>/", views.TextEditView.as_view(), name="edit_text"),
    re_path(r"(?P<quiz_pk>\d+)/create_question/(?P<question_type>mc|tf)/$",
            views.QuestionCreateView.as_view(), name="create_question"),
]
