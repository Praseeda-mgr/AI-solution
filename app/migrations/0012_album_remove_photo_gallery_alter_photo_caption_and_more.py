# Generated by Django 5.0.6 on 2024-12-09 04:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='gallery',
        ),
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='album_photos/'),
        ),
        migrations.AddField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='app.album'),
        ),
        migrations.DeleteModel(
            name='PhotoGallery',
        ),
    ]
