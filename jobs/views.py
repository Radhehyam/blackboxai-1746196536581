from django.shortcuts import render, get_object_or_404
from .models import Job
from django.db.models import Q

def job_list(request):
    query = request.GET.get('q')
    if query:
        jobs = Job.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query) |
            Q(company_name__icontains=query)
        ).order_by('-date_posted')
    else:
        jobs = Job.objects.all().order_by('-date_posted')
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'query': query})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})
