# Generated by Django 5.0.6 on 2024-12-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_solution_delete_softwaresolution'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastsolution',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='past_solutions/'),
        ),
    ]
