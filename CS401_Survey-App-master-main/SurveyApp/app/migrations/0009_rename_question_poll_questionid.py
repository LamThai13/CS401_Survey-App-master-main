# Generated by Django 4.2.3 on 2023-07-17 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_entity_is_active_remove_entity_is_permanent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='question',
            new_name='questionId',
        ),
    ]
