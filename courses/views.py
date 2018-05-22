from django.views import View
from django.http import HttpResponse


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Welcome to Learners Cafe")
