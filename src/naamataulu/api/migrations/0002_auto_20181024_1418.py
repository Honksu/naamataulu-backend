# Generated by Django 2.1.2 on 2018-10-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='face_features',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='face_recognition_implementer',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
