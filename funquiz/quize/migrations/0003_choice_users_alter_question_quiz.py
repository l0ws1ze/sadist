# Generated by Django 5.1.2 on 2024-10-31 14:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quize', '0002_alter_question_pub_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='choices', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quize.quiz'),
        ),
    ]
