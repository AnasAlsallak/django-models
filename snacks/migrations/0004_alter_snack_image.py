# Generated by Django 4.2.2 on 2023-06-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0003_snack_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='image',
            field=models.ImageField(default='static/default.jpg', upload_to='static/'),
        ),
    ]
