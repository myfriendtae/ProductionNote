# Generated by Django 3.0.4 on 2020-12-03 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itn', '0007_image'),
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
        migrations.DeleteModel(
            name='Image',
        ),
    ]