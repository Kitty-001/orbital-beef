# Generated by Django 5.0.6 on 2024-06-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='update_wallet',
            field=models.BooleanField(default=True),
        ),
    ]
