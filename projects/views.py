from django.http import HttpResponse
from django.template import loader
from .models import Project

def main(request):
    myprojects = Project.objects.all().values()
    template = loader.get_template('main.html')
    context = {
        'myprojects': myprojects,
    }
    return HttpResponse(template.render(context, request))

def project(request, name):
    myproject = Project.objects.get(name=name)
    template = loader.get_template(name + '.html')
    context = {
        'myproject': myproject,
    }
    return HttpResponse(template.render(context, request))

def arcade(request, name="arcade"):
    myproject = Project.objects.get(name=name)
    template = loader.get_template(name + '.html')
    context = {
        'myproject': myproject,
    }
    return HttpResponse(template.render(context, request))
