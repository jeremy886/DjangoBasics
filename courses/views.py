from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from . import models
from itertools import chain


class CourseListView(ListView):
    model = models.Course


class CourseDetailView(DetailView):
    model = models.Course
    template_name = "courses/course_detail.html"

    def get_context_data(self, **kwargs):
        course = super().get_queryset()
        course = course.get(id=self.kwargs["pk"])
        context = super().get_context_data(**kwargs)
        steps = sorted(
            chain(course.text_set.all(), course.quiz_set.all()),
            key=lambda step: step.order
        )
        context["steps"] = steps
        context["course"] = course
        return context


# from django.shortcuts import render, get_object_or_404
#
#
# def step_detail(request, **kwargs):
#     course_pk = kwargs["course_pk"]
#     step_pk = kwargs["step_pk"]
#     step = get_object_or_404(Step, course=course_pk, pk=step_pk)
#     return render(request, "courses/step_detail.html", {"step": step})


class TextDetailView(DetailView):

    model = models.Text
    query_pk_and_slug = True
    slug_field = "course"
    slug_url_kwarg = "course_pk"
    pk_url_kwarg = "step_pk"
    template_name = "courses/step_detail.html"


class QuizDetailView(DetailView):

    model = models.Quiz
    query_pk_and_slug = True
    slug_field = "course"
    slug_url_kwarg = "course_pk"
    pk_url_kwarg = "step_pk"
    template_name = "courses/step_detail.html"