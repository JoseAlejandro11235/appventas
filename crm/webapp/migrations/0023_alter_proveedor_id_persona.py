# Generated by Django 5.0 on 2023-12-26 21:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_alter_personatelefono_id_persona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='id_persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webapp.persona'),
        ),
    ]
