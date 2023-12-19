# Generated by Django 5.0 on 2023-12-19 03:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_categoriapadre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriapadre',
            name='id',
        ),
        migrations.AlterField(
            model_name='categoriapadre',
            name='id_categoriahijo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_padre_hijo', to='webapp.categoria'),
        ),
        migrations.AlterField(
            model_name='categoriapadre',
            name='id_categoriapadre',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='categoria_padre_padre', serialize=False, to='webapp.categoria'),
        ),
    ]