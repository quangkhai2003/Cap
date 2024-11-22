# Generated by Django 4.1.13 on 2024-11-07 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CapApp', '0012_alter_vocabulary_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocabulary',
            name='topic',
        ),
        migrations.AddField(
            model_name='vocabulary',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='CapApp.topic'),
            preserve_default=False,
        ),
    ]
