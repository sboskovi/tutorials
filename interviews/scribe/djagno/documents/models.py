from django.db import models
# NOTE: pogubljenost u guglanju, isao si u dokumentaciju da pokazes kako dobro ti baratas njome a zapravo bi ti prvi
# stack overflow odgovorio na pitanje
from django.contrib.auth import get_user_model

User = get_user_model()


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Default je null=False, blank=False
    # NOTE: Ti si pretpostavio suprotno!
    title = models.CharField(max_length=200, null=False, blank=False)


class Node(models.Model):
    # NOTE: related_name se koristi da bi mogao da uradis ovako nesto:
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="steps")
    # NOTE: URLField nisi znao da postoji, priznao si, ukucao i intelisense ti je izbacio prijedlog
    media_url = models.URLField(null=True, blank=True)
    # NOTE: Krenuo si sa CharField i zastao kod max_length. TextField nema ogranicenja velicine?
    description = models.TextField(null=True, blank=True)
    # NOTE: Nisi znao kako da definises strani kljuc na sam model - "self". Ime promjenljive ne moze da bude steps
    # Ali si znao sta trebas da uradis cim ti je objasnio sta hoce
    nodes = models.ForeignKey("self", related_name="steps", on_delete=models.CASCADE)
