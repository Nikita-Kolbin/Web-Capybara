# Generated by Django 4.2.1 on 2023-05-07 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_post_preview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['pk'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['pk'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='preview',
            new_name='preview_img',
        ),
    ]