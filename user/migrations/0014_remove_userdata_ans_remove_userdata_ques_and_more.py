# Generated by Django 4.1.1 on 2022-11-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_userdata_remove_profile_ans_remove_profile_ques_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='ans',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='ques',
        ),
        migrations.AddField(
            model_name='userdata',
            name='correct',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='userdata',
            name='percent',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='userdata',
            name='total',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='userdata',
            name='wrong',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user',
            field=models.CharField(default='', max_length=255),
        ),
    ]
