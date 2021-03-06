# Generated by Django 3.0.6 on 2020-05-27 19:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200512_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='posts_image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=40, validators=[django.core.validators.RegexValidator('^[, a-zA-Z]*$', 'Only space separate English letters are allowed.')]),
        ),
    ]
