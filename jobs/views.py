from django.shortcuts import render
from .models import Job


def home(request):
    jobs = Job.objects
    title = "Home"
    return render(request, 'jobs/home.html', {'jobs':jobs, 'title':title})
