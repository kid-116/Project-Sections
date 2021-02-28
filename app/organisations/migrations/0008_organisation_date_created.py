# Generated by Django 3.1.6 on 2021-02-21 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0007_auto_20210221_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
