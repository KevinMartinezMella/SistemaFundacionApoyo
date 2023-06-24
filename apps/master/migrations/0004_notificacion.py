# Generated by Django 4.2.2 on 2023-06-24 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_aportador_password_alter_aportador_fechacreacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=255)),
                ('fechaMensaje', models.DateField(auto_now_add=True)),
                ('aportador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='master.aportador')),
            ],
        ),
    ]