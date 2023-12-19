# Generated by Django 5.0 on 2023-12-19 03:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_categoriapadre_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriapadre',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoriapadre',
            name='id_categoriapadre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_padre_padre', to='webapp.categoria'),
        ),
    ]