from rest_framework.serializers import ModelSerializer

from documents.models import Document


class DocumentSerializer(ModelSerializer):
    # NOTE: Kako ukljuciti User-a u serializer i kako node-ove?

    class Meta:
        model = Document
        fields = "__all__"
