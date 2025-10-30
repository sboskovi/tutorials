from django.db import models


ITEM_TYPES = {i: x for i, x in enumerate(['Optical equipment', 'Microcontrollers', 'Software equipment'])}


class ItemModel(models.Model):
    name = models.CharField(max_length=200)
    item_type = models.CharField(choices=ITEM_TYPES, default=ITEM_TYPES[0], max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} | {self.item_type} | {self.created_at}"


class Company(models.Model):
    name = models.CharField(max_length=200)
    chair_no = models.IntegerField(null=True, blank=True, verbose_name="Number of chairs")
    employee_no = models.IntegerField(null=True, blank=True, verbose_name="Number of employees")

    def __str__(self):
        return f"{self.name} -> {self.chair_no} : {self.employee_no}"


class Employee(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.company.name}"


# Koliko si ovdje vremena izgubio boze mili
from django.contrib.auth import get_user_model
User = get_user_model()


class Document(models.Model):
    # null=False, blank=False je default, nisi mrao da pises
    title = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="documents")


class Node(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_names="steps")
    # TextField nema ogranicnja?
    description = models.TextField(null=False, blank=False)
    # URLField, nisi znao, ali si ga lako importovao
    media_url = models.URLField(null=True, blank=True)
    # ne moze ime promjenljive da bude steps, "self" nisi znao
    nodes = models.ForeignKey("self", related_name="steps", on_delete=models.CASCADE)
