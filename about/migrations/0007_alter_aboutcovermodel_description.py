# Generated by Django 3.2.5 on 2021-08-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_alter_aboutcovermodel_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcovermodel',
            name='description',
            field=models.CharField(max_length=128, null=True, verbose_name='description'),
        ),
    ]
