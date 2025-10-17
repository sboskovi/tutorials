from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from documents.models import Document, Node
from documents.serializers import DocumentSerializer
from documents.utils import create_document_from_data


class DocumentView(APIView):
    @staticmethod
    def get(_):
        documents = Document.objects.all()
        for document in documents:
            nodes = Node.objects.filter(document=document.id)
        # serialized = DocumentSerializer(documents, many=True)
        # return Response(serialized.data)
        return JsonResponse()

    @staticmethod
    def post(request):
        create_document_from_data(None, request.data)
        return JsonResponse({'message': "Created"}, status=status.HTTP_201_CREATED)


