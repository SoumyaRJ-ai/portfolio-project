# Generated by Django 3.1.2 on 2020-10-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_body',
            field=models.TextField(),
        ),
    ]
