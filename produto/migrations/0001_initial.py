# Generated by Django 5.1.2 on 2024-11-06 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('descricao', models.CharField(max_length=15)),
                ('preco', models.CharField(max_length=60)),
                ('quantidade', models.CharField(max_length=60)),
            ],
        ),
    ]
