# Generated by Django 5.0.1 on 2024-02-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_uname_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='static/images/default.png', upload_to='user_images/'),
        ),
    ]
