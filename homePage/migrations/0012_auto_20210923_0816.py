# Generated by Django 3.2.5 on 2021-09-23 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0011_delete_bannermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='message_en',
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='message_ru',
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='message_uz',
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='name_uz',
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
