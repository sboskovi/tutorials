from django.contrib.auth import get_user_model

from documents.models import Document, Node

User = get_user_model()

documents_example = [
    {
        "title": "How to make a youtube video",
        "steps": [
            {
                "description": "..."
            },
            {
                "description": "...",
                "media_url": "...",
                "steps": [
                    {
                        "description": "..."
                    },
                    {
                        "description": "...",
                        "media_url": "..."
                    }
                ]
            }
        ]
    }
]


def create_document_from_data(_user, data):
    user = User.objects.get(username="stefan")
    # NOTE: ne moras da pozivas doc.save()! .create() obavi i save()
    for document in data:
        doc = Document.objects.create(
            user=user,
            title=document.get("title")
        )
        for node in document.get("steps", []):
            Node.objects.create(
                document=doc,
                description=node.get("description"),
                media_url=node.get("media_url")
            )


# NOTE: Treba da ukljci i Node-ove. Probao si preko serializer-a i pogubio si se,
# U python-u si ga odradio ocas posla
def get_document(document_id):
    document = Document.objects.get(pk=document_id)
    return document
