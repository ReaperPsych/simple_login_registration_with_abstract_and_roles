# Generated by Django 4.2.6 on 2023-10-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.IntegerField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('admin', 'Admin')]),
        ),
    ]