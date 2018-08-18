# Generated by Django 2.0.3 on 2018-08-18 15:39

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardid',
            name='dashboard_id',
            field=models.CharField(default=users.models.DashboardId.generate_custom_id, max_length=32, verbose_name='auth.User'),
        ),
    ]