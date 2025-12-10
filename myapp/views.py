from django.shortcuts import render
from django.views import View
from .models import Project, About


def home(request):
    """Display home page with featured projects"""
    featured_projects = Project.objects.filter(featured=True)
    context = {
        'featured_projects': featured_projects,
    }
    return render(request, 'myapp/home.html', context)


def portfolio(request):
    """Display all projects"""
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'myapp/portfolio.html', context)


def project_detail(request, pk):
    """Display single project details"""
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
    }
    return render(request, 'myapp/project_detail.html', context)


def about(request):
    """Display about page"""
    about_info = About.objects.first()
    context = {
        'about': about_info,
    }
    return render(request, 'myapp/about.html', context)
