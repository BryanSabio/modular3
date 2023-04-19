# Generated by Django 4.2 on 2023-04-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoGigante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marca', models.CharField(max_length=200)),
                ('adquirir', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=400)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoGrande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marca', models.CharField(max_length=200)),
                ('adquirir', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=400)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoMediano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marca', models.CharField(max_length=200)),
                ('adquirir', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=400)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoPequeno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marca', models.CharField(max_length=200)),
                ('adquirir', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=400)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
