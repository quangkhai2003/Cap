# Generated by Django 4.1.13 on 2024-11-06 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CapApp', '0003_alter_vocabulary_examples'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocabulary',
            name='examples',
        ),
    ]