from django.db import models
from django.contrib.auth.models import Group, Permission

# Create your models here.
Librarian, created = Group.objects.get_or_create(name='Librarian')

MODELS = ['book', 'book instance', 'author', 'requested books']
PERMISSIONS = ['view', 'add', 'delete', 'change']
for model in MODELS:
    for permission in PERMISSIONS:
        name = f'Can {permission} {model}'

        try:
            model_add_perm = Permission.objects.get(name=name)
        except Permission.DoesNotExist:
            continue

        Librarian.permissions.add(model_add_perm)
