# Generated by Django 5.0.6 on 2024-12-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_pastsolution_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastsolution',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
