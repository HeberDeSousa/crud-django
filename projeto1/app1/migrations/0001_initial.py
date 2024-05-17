# Generated by Django 5.0.6 on 2024-05-16 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='nome')),
                ('telefone', models.CharField(max_length=15, verbose_name='telefone')),
                ('email', models.CharField(max_length=30, verbose_name='email')),
                ('idade', models.IntegerField(verbose_name='idade')),
            ],
        ),
    ]