# Generated by Django 3.0.6 on 2020-07-19 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='aff_link',
            new_name='affiliate_link',
        ),
    ]
