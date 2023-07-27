# Generated by Django 4.2.1 on 2023-07-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la funcionalidad.', max_length=255, verbose_name='Nombre')),
                ('descripcion', models.TextField(help_text='Descripción de la funcionalidad.', verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Funcionalidad',
                'verbose_name_plural': 'Funcionalidades',
            },
        ),
        migrations.CreateModel(
            name='Subscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(help_text='Tipo de suscripción.', max_length=255, verbose_name='Tipo')),
                ('fecha_emision', models.DateField(help_text='Fecha de emisión de la suscripción', verbose_name='Fecha emisión')),
                ('fecha_caducidad', models.DateField(help_text='Fecha de caducidad de la suscripción', verbose_name='Fecha de caducidad')),
                ('precio', models.DecimalField(decimal_places=2, help_text='Precio de la suscripción', max_digits=10, verbose_name='Precio de la suscripción')),
                ('funcionalidades', models.ManyToManyField(help_text='Funcionalidades de la suscripción.', to='suscripciones.funcionalidad')),
            ],
            options={
                'verbose_name': 'Suscripción',
                'verbose_name_plural': 'Suscripciones',
            },
        ),
    ]
