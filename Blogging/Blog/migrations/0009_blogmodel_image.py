# Generated by Django 3.1.1 on 2020-09-18 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_likeblog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
