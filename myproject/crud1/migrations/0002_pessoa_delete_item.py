# Generated by Django 5.1.1 on 2024-09-13 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dt_nasc', models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
