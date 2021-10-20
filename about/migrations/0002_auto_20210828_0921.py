# Generated by Django 3.2.5 on 2021-08-28 04:21

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField(verbose_name='video')),
            ],
            options={
                'verbose_name': 'about',
                'verbose_name_plural': 'about',
            },
        ),
        migrations.DeleteModel(
            name='AboutModel',
        ),
    ]
