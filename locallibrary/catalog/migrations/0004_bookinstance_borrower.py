# Generated by Django 3.1.6 on 2021-02-06 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_auto_20210206_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
