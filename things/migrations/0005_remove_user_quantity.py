# Generated by Django 4.2.6 on 2023-10-10 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0004_alter_user_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='quantity',
        ),
    ]
