# Generated by Django 5.0 on 2023-12-19 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_rename_id_tipo_documento_persona_id_tipodocumento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=100)),
            ],
        ),
    ]
