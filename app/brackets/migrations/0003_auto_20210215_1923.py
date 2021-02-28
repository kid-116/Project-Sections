# Generated by Django 3.1.6 on 2021-02-15 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0003_auto_20210215_1858'),
        ('brackets', '0002_auto_20210214_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='bracket',
            name='organisation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brackets', to='organisations.organisation'),
        ),
        migrations.AlterField(
            model_name='bracket',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='JoinRequest',
        ),
    ]