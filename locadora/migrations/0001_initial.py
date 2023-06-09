# Generated by Django 4.2.1 on 2023-05-27 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locadora.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('filmes', models.ManyToManyField(to='locadora.filme')),
            ],
            options={
                'verbose_name': 'Locação',
                'verbose_name_plural': 'Locações',
            },
        ),
    ]
