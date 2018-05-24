from django.views.generic import ListView, DetailView

from .models import Course, Step


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


from django.shortcuts import render, get_object_or_404


# def step_detail(request, **kwargs):
#     course_pk = kwargs["course_pk"]
#     step_pk = kwargs["step_pk"]
#     step = get_object_or_404(Step, course=course_pk, pk=step_pk)
#     return render(request, "courses/step_detail.html", {"step": step})

class StepDetailView(DetailView):

    model = Step
    query_pk_and_slug=True
    slug_field = 'course'
    slug_url_kwarg = 'course_pk'
    pk_url_kwarg = 'step_pk'

