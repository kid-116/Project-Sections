# Generated by Django 3.1.6 on 2021-02-21 15:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organisations', '0006_auto_20210216_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisation',
            name='administrator',
        ),
        migrations.AddField(
            model_name='organisation',
            name='admins',
            field=models.ManyToManyField(related_name='admin_of', to=settings.AUTH_USER_MODEL),
        ),
    ]