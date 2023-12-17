# Generated by Django 4.1.1 on 2022-11-08 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0012_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('ques', models.CharField(max_length=255)),
                ('ans', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ans',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='ques',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]