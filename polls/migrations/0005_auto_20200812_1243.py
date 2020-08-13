# Generated by Django 3.0.7 on 2020-08-12 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200811_1304'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.RenameField(
            model_name='customs',
            old_name='color_darker',
            new_name='colors',
        ),
        migrations.RemoveField(
            model_name='customs',
            name='color_lighter',
        ),
        migrations.RemoveField(
            model_name='customs',
            name='department',
        ),
    ]