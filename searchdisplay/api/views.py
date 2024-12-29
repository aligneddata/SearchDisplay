from django.db import models
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import os
import logging
from .models import Document

logger = logging.getLogger('searchdisplay')

@csrf_exempt
def upload_document(request):
    if request.method == 'POST':
        file = request.FILES['file']
        converted_text = request.POST['converted_text']

        # Save file to file system
        fs = FileSystemStorage()
        saved_filename = fs.save(file.name, file)  # Get the actual saved filename
        saved_file_path = fs.path(saved_filename)  # Construct the absolute path

        logging.info("Saved file from [%s] is [%s], where full path [%s]" % 
                     (file.name, saved_filename, saved_file_path))
        # Create and save document record
        document = Document(
            filename=saved_filename, #file.name,
            type=os.path.splitext(file.name)[1][1:],
            text=converted_text,
            full_path=saved_file_path
        )
        document.save()

        return JsonResponse({"status": "success", "message": "Document uploaded successfully."})
    return JsonResponse({"status": "failure", "message": "Invalid request method."})


def get_documents(request):
    if request.method == 'GET':
        documents = Document.objects.all()
        documents_data = [
            {
                "id": doc.id,
                "original_filename": doc.original_filename,
                "document_type": doc.document_type,
                "full_path": doc.full_path,
                "created_date": doc.created_date
            } for doc in documents
        ]
        return JsonResponse({"documents": documents_data})


def create(request):
    pass


def search(request):
    query = request.GET.get('query', '')
    results = Document.objects.filter(text__icontains=query)
    results_data = [
        {
            "id": result.id,
            "filename": result.filename,
            "converted_text": result.text,
            "full_path": result.full_path
        } for result in results
    ]
    return JsonResponse({"results": results_data})
