# Generated by Django 4.2 on 2023-04-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
