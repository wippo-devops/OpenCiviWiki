# Generated by Django 2.2.16 on 2021-05-27 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_auto_20210526_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='civi',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='civi',
            name='linked_bills',
        ),
        migrations.RemoveField(
            model_name='rationale',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='rationale',
            name='vote',
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
