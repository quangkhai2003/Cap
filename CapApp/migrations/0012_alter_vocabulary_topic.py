# Generated by Django 4.1.13 on 2024-11-07 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CapApp', '0011_alter_vocabulary_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocabulary',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic', to='CapApp.topic'),
        ),
    ]
