# Generated by Django 4.1.4 on 2023-01-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierecommenderapp', '0002_rename_show_id_rating_show_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watched',
            old_name='show_id',
            new_name='show',
        ),
        migrations.RenameField(
            model_name='watched',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='rating',
            name='show',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.IntegerField(),
        ),
    ]
