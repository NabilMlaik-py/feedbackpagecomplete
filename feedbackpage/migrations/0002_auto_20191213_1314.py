# Generated by Django 3.0 on 2019-12-13 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbackperson',
            old_name='feedback_msg',
            new_name='feedback',
        ),
    ]
