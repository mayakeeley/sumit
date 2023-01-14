from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist


def index(request):
    try:
        return render(request, "index.html")
    except TemplateDoesNotExist:
        return render(request, "core/index-placeholder.html")
