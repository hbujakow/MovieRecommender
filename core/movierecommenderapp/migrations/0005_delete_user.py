# Generated by Django 4.1.4 on 2023-01-15 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movierecommenderapp', '0004_user_is_email_verified'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]