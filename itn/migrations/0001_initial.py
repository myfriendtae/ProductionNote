# Generated by Django 3.0.4 on 2021-01-07 08:55

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('group', models.CharField(max_length=50)),
                ('file', models.FileField(blank=True, upload_to='itn/')),
                ('signed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NightEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('edit_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('night_content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('group', models.CharField(max_length=50)),
                ('editor', models.CharField(max_length=50)),
                ('signed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DayEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('edit_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('day_content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('group', models.CharField(max_length=50)),
                ('editor', models.CharField(max_length=50)),
                ('signed_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]