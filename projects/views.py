from django.shortcuts import render


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
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
