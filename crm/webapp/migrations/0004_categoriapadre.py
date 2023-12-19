# Generated by Django 5.0 on 2023-12-19 03:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPadre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_categoriahijo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.categoria')),
                ('id_categoriapadre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.categoriapadre')),
            ],
        ),
    ]
