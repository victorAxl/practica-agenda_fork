# Generated by Django 2.2.24 on 2021-09-05 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=120)),
                ('fotografia', models.ImageField(upload_to='')),
                ('fecha_nacio', models.DateField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, 'Casa'), (2, 'Teléfono móvil')])),
                ('alias', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=50)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.Contacto')),
            ],
            options={
                'verbose_name': 'Teléfono',
                'verbose_name_plural': 'Teléfonos',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=255)),
                ('numero_exterior', models.CharField(max_length=10)),
                ('numero_interior', models.CharField(max_length=10)),
                ('colonia', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[('AGU', 'Aguascalientes'), ('BCN', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAM', 'Campeche'), ('CHP', 'Chiapas'), ('CHH', 'Chihuahua'), ('CMX', 'Ciudad de México'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DUR', 'Durango'), ('GUA', 'Guanajuato'), ('GRO', 'Guerrero'), ('HID', 'Hidalgo'), ('JAL', 'Jalisco'), ('MEX', 'México'), ('MIC', 'Michoacán'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NLE', 'Nuevo León'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QUE', 'Querétaro'), ('ROO', 'Quintana Roo'), ('SLP', 'San Luis Potosí'), ('SIN', 'Sinaloa'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLA', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucatán'), ('ZAC', 'Zacatecas')], max_length=3)),
                ('referencias', models.TextField()),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.Contacto')),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Direcciones',
            },
        ),
    ]
