# Generated by Django 3.1.1 on 2020-10-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20201008_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admindata',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='education_detail',
            name='Int_percent',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='education_detail',
            name='sec_percent',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='graduation',
            name='sem1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='graduation',
            name='sem2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='graduation',
            name='sem3',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='graduation',
            name='sem4',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='graduation',
            name='sem5',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='graduation',
            name='sem6',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='graduation',
            name='sem7',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='graduation',
            name='sem8',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]