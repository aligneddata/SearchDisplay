from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template = loader.get_template("web/index.html")
    context = {
        "var1": "12345",
    }
    return HttpResponse(template.render(context, request))
