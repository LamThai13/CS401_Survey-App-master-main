# Generated by Django 4.2.3 on 2023-07-10 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_rate_date_remove_rate_rate_remove_rate_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='user',
        ),
    ]
