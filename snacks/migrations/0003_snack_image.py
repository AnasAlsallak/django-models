# Generated by Django 4.2.2 on 2023-06-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0002_alter_snack_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
