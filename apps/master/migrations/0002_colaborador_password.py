# Generated by Django 4.2.2 on 2023-06-24 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
