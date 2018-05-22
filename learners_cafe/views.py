from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse


class HelloView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World!")


class HomeView(TemplateView):
    template_name = "home.html"