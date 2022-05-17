# Generated by Django 4.0.4 on 2022-05-17 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rareV2Api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='postreactions',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='postreactions',
            old_name='reaction_id',
            new_name='reaction',
        ),
        migrations.RenameField(
            model_name='postreactions',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='posttags',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='posttags',
            old_name='tag_id',
            new_name='tag',
        ),
    ]