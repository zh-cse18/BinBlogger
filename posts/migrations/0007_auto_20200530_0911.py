# Generated by Django 3.0.6 on 2020-05-30 09:11

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20200530_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_thumbnail',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format=None, keep_meta=True, quality=90, size=[800, 580], upload_to='posts_image'),
        ),
    ]
