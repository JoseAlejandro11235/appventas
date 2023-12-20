# Generated by Django 5.0 on 2023-12-20 19:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_remove_personadireccion_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_sunat', models.CharField(max_length=2)),
                ('denominacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PersonaOficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_oficio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.oficio')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.persona')),
            ],
        ),
    ]
