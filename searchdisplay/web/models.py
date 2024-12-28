from django.db import models
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import os
from api.models import Document

