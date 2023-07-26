# Generated by Django 4.2.3 on 2023-07-23 20:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_question_poll_questionid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
        migrations.AddField(
            model_name='entity',
            name='rate_question',
            field=models.TextField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='rating',
            name='rate_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.entity'),
        ),
    ]