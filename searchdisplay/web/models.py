from django.db import models
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import os
from api.models import Document


# Search View
class SearchView(View):

    def get(self, request):
        query = request.GET.get('query', '')
        results = Document.objects.filter(converted_text__icontains=query)
        results_data = [
            {
                "id": result.id,
                "original_filename": result.original_filename,
                "converted_text": result.converted_text,
                "full_path": result.full_path
            } for result in results
        ]
        return JsonResponse({"results": results_data})

    def home(request):
        return render(request, 'home.html')