from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class ResumePageView(TemplateView):
    template_name = "pages/resume.html"

def info(request):
    return render(request, 'pages/resume.html', {'message': 1111111111111})