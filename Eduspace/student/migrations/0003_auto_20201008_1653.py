# Generated by Django 3.1.1 on 2020-10-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_admin_login_admindata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(upload_to='student/profile_img/'),
        ),
    ]
