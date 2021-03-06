# Generated by Django 3.0.6 on 2020-05-30 09:24

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200530_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default.jpg', force_format=None, keep_meta=False, quality=85, size=[300, 300], upload_to='profile_pics', verbose_name='profile_pic'),
        ),
    ]
