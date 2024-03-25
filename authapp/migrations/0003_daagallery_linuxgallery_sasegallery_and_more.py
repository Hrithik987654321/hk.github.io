# Generated by Django 4.2.6 on 2024-03-24 05:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_phpgallery_contactmessage_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaaGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='daa_pdfs')),
                ('timeStamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='LinuxGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='linux_pdfs')),
                ('timeStamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='SaseGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='sase_pdfs')),
                ('timeStamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='StatisticsGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='statistics_pdfs')),
                ('timeStamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
