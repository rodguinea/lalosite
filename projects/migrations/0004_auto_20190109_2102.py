# Generated by Django 2.1.4 on 2019-01-10 07:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190103_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='english_bio',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='bio',
            name='spanish_bio',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
