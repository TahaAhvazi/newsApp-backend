# Generated by Django 4.0.4 on 2022-05-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='NoImage', upload_to=''),
        ),
    ]
