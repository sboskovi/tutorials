from django.urls import path

from documents.views import DocumentView

urlpatterns = [
    path('', DocumentView.as_view()),
]
