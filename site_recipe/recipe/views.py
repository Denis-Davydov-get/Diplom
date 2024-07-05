import logging

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    logger.info(msg="")
    return render(request, "recipe/index.html", {"title": "Homepage"})


def about(request):
    logger.info(msg="")
    return HttpResponse("About us")
