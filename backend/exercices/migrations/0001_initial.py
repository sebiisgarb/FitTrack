# Generated by Django 5.1 on 2024-10-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('muscle_group', models.CharField(max_length=50)),
                ('video_url', models.CharField(max_length=100)),
            ],
        ),
    ]
