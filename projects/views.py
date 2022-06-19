from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import search_projects, paginate_project


def projects(request):
    projects_list, search_query = search_projects(request)
    custom_range, projects_list = paginate_project(request, projects_list, 6)

    context = {
        'projects': projects_list,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project_obj
        review.owner = request.user.profile
        review.save()

        project_obj.get_vote_count

        messages.success(request, 'Your review was successfully submitted!')

        return redirect('project', pk=project_obj.id)

    return render(request, 'projects/single-project.html', {'project_obj': project_obj, 'form': form})


@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/projects-form.html', context)


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project_obj = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project_obj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project_obj)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/projects-form.html', context)


@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project_obj = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project_obj.delete()
        return redirect('projects')
    context = {'object': project_obj}
    return render(request, 'delete-template.html', context)
