# Generated by Django 3.2 on 2021-04-24 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0008_requestedbooks_requester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestedbooks',
            name='requester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
