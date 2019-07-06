from django.shortcuts import render, get_object_or_404
from .models import Job, Formations, skills


def home(request):
    jobs = Job.objects
    formations = Formations.objects
    skillsinformatic = skills.objects
    return render(request, 'jobs/home.html', {'jobs':jobs, 'formations': formations, 'skillsinformatic':skillsinformatic})

def detailjobs(request, jobs_id):
    detailjobs = get_object_or_404(Job, pk=jobs_id)
    return render(request, 'jobs/detailjobs.html', {'jobs':detailjobs})

