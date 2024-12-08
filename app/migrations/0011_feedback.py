# Generated by Django 5.0.6 on 2024-12-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_pastsolution_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
