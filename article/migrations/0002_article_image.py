# Generated by Django 4.0.4 on 2022-05-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='No image', upload_to=''),
        ),
    ]