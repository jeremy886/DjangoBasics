from itertools import chain

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms


class CourseListView(ListView):
    model = models.Course


class CourseDetailView(DetailView):
    model = models.Course
    template_name = "courses/course_detail.html"

    def get_context_data(self, **kwargs):
        # course = super().get_queryset()
        course = get_object_or_404(models.Course, id=self.kwargs["pk"])
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
    template_name = "courses/text_detail.html"


class QuizDetailView(DetailView):

    model = models.Quiz
    query_pk_and_slug = True
    slug_field = "course"
    slug_url_kwarg = "course_pk"
    pk_url_kwarg = "step_pk"
    template_name = "courses/quiz_detail.html"
    # # once you define context_object_name "quiz", quiz_detail.html matches the default
    # # template name, so you don't need it anymore.
    # template_name = "courses/quiz_detail.html"


class QuizCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = "course"
    pk_url_kwarg = "course_pk"
    context_object_name = 'course'
    form_class = forms.QuizForm
    template_name = "courses/quiz_create.html"
    success_message = "%(title)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_pk = self.kwargs.get(self.pk_url_kwarg)
        course = get_object_or_404(models.Course, pk=course_pk)
        context["course"] = course
        return context

    def form_valid(self, form):
        course_pk = self.kwargs.get(self.pk_url_kwarg)
        form.instance.course = get_object_or_404(models.Course, pk=course_pk)
        return super().form_valid(form)

    def get_success_url(self):
        course_pk = self.kwargs["course_pk"]
        return reverse_lazy('courses:detail', kwargs={'pk': course_pk})
        # More: how to get the quiz id from the above quiz form


class QuizEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    query_pk_and_slug = True
    slug_field = "course"
    slug_url_kwarg = "course_pk"
    pk_url_kwarg = "quiz_pk"
    model = models.Quiz
    form_class = forms.QuizForm
    success_message = "%(title)s was updated successfully"
    template_name = "courses/quiz_edit.html"


class TextEditView(LoginRequiredMixin, UpdateView):
    """To be added"""


class QuestionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    deal with both multiple choice questiona and true/false questions,
    from re_path patterns in one view.
    """
    pk_url_kwarg = "quiz_pk"
    success_message = "%(prompt)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz_pk = self.kwargs.get(self.pk_url_kwarg)
        quiz = get_object_or_404(models.Quiz, pk=quiz_pk)
        context["quiz"] = quiz
        return context

    def form_valid(self, form):
        quiz_pk = self.kwargs.get(self.pk_url_kwarg)
        form.instance.quiz = get_object_or_404(models.Quiz, pk=quiz_pk)
        return super().form_valid(form)


class MCQuestionCreateView(QuestionCreateView):
    form_class = forms.MultipleChoiceQuestionForm
    template_name = "courses/question_form.html"


class TFQuestionCreateView(QuestionCreateView):
    form_class = forms.TrueFalseQuestionForm
    template_name = "courses/question_form.html"


class QuestionEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    query_pk_and_slug = True
    slug_field = "quiz"
    slug_url_kwarg = "quiz_pk"
    pk_url_kwarg = "question_pk"
    success_message = "%(prompt)s was updated successfully"
    template_name = "courses/question_edit.html"


class MCQuestionEditView(QuestionEditView):
    model = models.MultipleChoiceQuestion
    form_class = forms.MultipleChoiceQuestionForm


class TFQuestionEditView(QuestionEditView):
    model = models.TrueFalseQuestion
    form_class = forms.TrueFalseQuestionForm

