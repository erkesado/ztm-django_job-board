from django.shortcuts import render, get_object_or_404

from .models import JobPosting

# Create your views here.
def index(request):
    active_posts = JobPosting.objects.filter(is_active=True)
    context = {
        'job_posts': active_posts,
    }
    return render(request, 'index.html', context)

def job_detail(request, id):
    job_post = get_object_or_404(JobPosting, id=id, is_active=True)
    context = {
        'job_post': job_post,
    }
    return render(request, 'detail.html', context)
