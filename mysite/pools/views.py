from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from pools.models import Pools

def index(request):
    title = ''
    for pools in Pools.objects.all():
        title = pools
    context = RequestContext(request, {
        'title': title,
    })
    template = loader.get_template('pools/index.html')
    return HttpResponse(template.render(context))
