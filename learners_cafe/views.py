from django.views import View
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

from . import forms


class HelloView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World!")


class HomeView(TemplateView):
    template_name = "home.html"


class SuggestionFormView(FormView):
    form_class = forms.SuggestionForm
    template_name = "suggestion_form.html"
    success_url = reverse_lazy("suggestion")

    def form_valid(self, form):
        msg = form.cleaned_data
        send_mail(
            f"Suggestion from {msg['name']}",
            f"{msg['suggestion']}",
            f"{msg['name']} <{msg['email']}>",
            ["jeremy@learners.cafe"],
        )
        messages.success(self.request, "Thank you for your suggestion!")
        return super().form_valid(form)
