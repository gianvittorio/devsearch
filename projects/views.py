from django.shortcuts import render
from .models import Project


projectsList = [
    {
        'id': '1',
        'title': 'E-commerce Website',
        'description': 'Fully functional e-commerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This is a project where I built my portfolio'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I am still working on'
    },
]


def projects(request):
    projects_list = Project.objects.all()
    context = {'projects': projects_list}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    tags = project_obj.tags.all()
    return render(request, 'projects/single-project.html', {'project_obj': project_obj})
