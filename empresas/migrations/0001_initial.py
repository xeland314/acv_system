# Generated by Django 4.2.1 on 2023-07-12 03:48

from django.db import migrations, models
import django.db.models.deletion
import usuarios.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suscripciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_comercial', models.CharField(help_text='Nombre comercial de la empresa.', max_length=255, verbose_name='Nombre comercial')),
                ('ruc', models.CharField(help_text='RUC de la empresa.', max_length=13, verbose_name='RUC')),
                ('direccion', models.TextField(help_text='Dirección de la empresa.', verbose_name='Dirección')),
                ('correo', models.EmailField(help_text='Correo electrónico de la empresa.', max_length=100, verbose_name='Correo electrónico')),
                ('telefono', models.CharField(help_text='Teléfono de la empresa.', max_length=15, validators=[usuarios.validators.validar_numero_de_telefono], verbose_name='Teléfono')),
                ('logo_empresa', models.ImageField(blank=True, help_text='Logo de la empresa.', null=True, upload_to='', verbose_name='Logo de la empresa')),
                ('suscripcion', models.OneToOneField(help_text='Suscripción de la empresa.', on_delete=django.db.models.deletion.CASCADE, to='suscripciones.subscripcion')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]
