# Generated by Django 5.0.9 on 2024-10-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'categoria',
            },
        ),
    ]
