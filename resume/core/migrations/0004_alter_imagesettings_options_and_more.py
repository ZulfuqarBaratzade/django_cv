# Generated by Django 4.2.1 on 2023-06-11 15:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_imagesettings'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesettings',
            options={'ordering': ('name',), 'verbose_name': 'Image Settings', 'verbose_name_plural': 'Image Settings'},
        ),
        migrations.AddField(
            model_name='imagesettings',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created_date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagesettings',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='update_date'),
        ),
    ]