# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 02:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0009_auto_20171104_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_pedido',
            name='pedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Pedido'),
        ),
    ]