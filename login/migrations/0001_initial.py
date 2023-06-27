# Generated by Django 4.2.1 on 2023-06-27 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import login.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suscripciones', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_comercial', models.CharField(help_text='Nombre comercial de la empresa.', max_length=255, verbose_name='Nombre comercial')),
                ('ruc', models.CharField(help_text='RUC de la empresa.', max_length=13, verbose_name='RUC')),
                ('direccion', models.CharField(help_text='Dirección de la empresa.', max_length=200, verbose_name='Dirección')),
                ('correo', models.EmailField(help_text='Correo electrónico de la empresa.', max_length=100, verbose_name='Correo electrónico')),
                ('telefono', models.CharField(help_text='Teléfono de la empresa.', max_length=15, validators=[login.models.validar_numero_de_telefono], verbose_name='Teléfono')),
                ('suscripcion', models.OneToOneField(help_text='Suscripción de la empresa.', on_delete=django.db.models.deletion.CASCADE, to='suscripciones.subscripcion')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(help_text='Nombres de la persona.', max_length=150, validators=[login.models.validar_nombres_apellidos], verbose_name='Nombres')),
                ('apellidos', models.CharField(help_text='Apellidos de la persona.', max_length=150, verbose_name='Apellidos')),
                ('cedula', models.CharField(help_text='Cédula de la persona.', max_length=10, validators=[login.models.validar_cedula], verbose_name='Cédula')),
                ('email', models.EmailField(help_text='Email de la persona.', max_length=100, verbose_name='Email')),
                ('telefono', models.CharField(help_text='Teléfono de la persona.', max_length=15, validators=[login.models.validar_numero_de_telefono], verbose_name='Teléfono')),
                ('direccion', models.TextField(blank=True, help_text='Dirección de la persona.', verbose_name='Dirección')),
                ('fecha_nacimiento', models.DateField(help_text='Fecha de nacimiento de la persona.', validators=[login.models.validar_fecha_de_nacimiento], verbose_name='Fecha de nacimiento')),
                ('nivel_educacion', models.CharField(choices=[('General Básica', 'GENERAL_BASICA'), ('Bachillerato', 'BACHILLERATO'), ('Superior', 'SUPERIOR')], help_text='Nivel de educación de la persona.', max_length=30, verbose_name='Nivel de educación')),
                ('estado_civil', models.CharField(choices=[('Casado', 'CASADO'), ('Divorciado', 'DIVORCIADO'), ('Soltero', 'SOLTERO'), ('Unión Libre', 'UNION_LIBRE'), ('Viudo', 'VIUDO')], help_text='Estado civil de la persona.', max_length=20, verbose_name='Estado Civil')),
                ('fotografia', models.ImageField(blank=True, help_text='Fotografía opcional de la persona.', null=True, upload_to='', verbose_name='Fotografía')),
                ('empresa', models.ForeignKey(help_text='Empresa en la que labora el trabajador.', on_delete=django.db.models.deletion.CASCADE, related_name='trabajadores', to='login.empresa')),
                ('user', models.OneToOneField(help_text='Relación uno a uno con el modelo User de Django.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
            },
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('trabajador_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='login.trabajador')),
                ('ruc', models.CharField(help_text='RUC del representante.', max_length=13, verbose_name='RUC')),
            ],
            options={
                'verbose_name': 'Representante',
                'verbose_name_plural': 'Representantes',
            },
            bases=('login.trabajador',),
        ),
    ]
