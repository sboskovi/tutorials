from base.models import Document, Node


documents_example = [
    {
        "title": "How to make a youtube video",
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


# NOTE: pogubio si se ovdje sa serializer-ima i kako odraditi ovo s njima
def create_documents(user, documents):
    for doc in documents:
        document = Document.objects.create(
            user=user,
            title=doc.get("title")
        )

        for step in documents.get("steps"):
            Node.create(
                document=document,
                description=step.get("description"),
                media_url=step.get("media_url", None)
            )


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


def get_document(document_id):
    document = Document.objects.get(pk=document_id)
    return document
