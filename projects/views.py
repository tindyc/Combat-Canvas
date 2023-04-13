from django.shortcuts import render
from django.http import HttpResponse


projectsList = [

{'id': '1', 'title': 'Art project 1', 'description': 'description for art project 1' },

{ 'id': '2', 'title': 'Art project 2', 'description': 'description for art project 2' },

{'id': '3', 'title': 'Art project 3', 'description': 'description for art project 3' }

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
