# Generated by Django 5.0.2 on 2024-02-22 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='pagina',
        ),
    ]