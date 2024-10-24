# Generated by Django 5.0.9 on 2024-10-17 18:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Enderecos', '0002_alter_endereco_table'),
        ('categorias', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.BigIntegerField()),
                ('descricao', models.TextField()),
                ('foto_local', models.ImageField(blank=True, null=True, upload_to='estabelecimentos/fotos/')),
                ('media_avaliacao', models.FloatField(default=0.0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.categoria')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Enderecos.endereco')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'estabelecimento',
            },
        ),
    ]
