# Generated by Django 4.2.7 on 2023-11-30 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_aboutcard_introcard_delete_card_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutcard',
            old_name='descripition',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='introcard',
            old_name='descripition',
            new_name='description',
        ),
    ]
