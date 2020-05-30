# Generated by Django 3.0.6 on 2020-05-30 10:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_delete_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='nickname',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
