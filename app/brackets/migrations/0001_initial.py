# Generated by Django 3.1.6 on 2021-02-14 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bracket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('graduation_year', models.IntegerField()),
                ('cr', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cr_of', to=settings.AUTH_USER_MODEL)),
                ('faculty_advisor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='facadv_of', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(blank=True, related_name='brackets', to=settings.AUTH_USER_MODEL, verbose_name='Member')),
            ],
        ),
        migrations.CreateModel(
            name='JoinRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=None, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('slug', models.SlugField(default=None, null=True)),
                ('account', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='join_requests', to=settings.AUTH_USER_MODEL)),
                ('bracket', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='join_requests', to='brackets.bracket')),
            ],
        ),
    ]