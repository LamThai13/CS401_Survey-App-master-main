# Generated by Django 4.2.3 on 2023-07-25 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='rate_question',
        ),
    ]
