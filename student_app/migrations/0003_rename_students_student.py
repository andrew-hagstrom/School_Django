# Generated by Django 4.2.7 on 2023-11-20 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_alter_students_personal_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
    ]