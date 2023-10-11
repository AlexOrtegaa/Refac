# Generated by Django 4.2.6 on 2023-10-10 21:33

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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Ingresa el título del proyecto.', max_length=200)),
                ('summary', models.TextField(default='', help_text='Ingresa una descripción de la inversión.', max_length=1000)),
                ('mini_summary', models.TextField(default='', help_text='Ingresa una descripción breve de la inversión. No más de 50 carácteres.', max_length=50)),
                ('company', models.CharField(help_text='Ingresa el nombre de la compañía que dirige el proyecto.', max_length=200)),
                ('date_published', models.DateField(blank=True, help_text='Fecha de publicación.', null=True)),
                ('interest_rate', models.DecimalField(decimal_places=8, default=0, max_digits=10)),
            ],
            options={
                'permissions': (('can_add_proyect', 'Puede añadir proyecto'),),
            },
        ),
        migrations.CreateModel(
            name='ProjectInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_acquired', models.DateField(blank=True, help_text='Fecha de unión al proyecto', null=True)),
                ('date_of_end_contract', models.DateField(blank=True, help_text='Fecha de fin de unión al proyecto', null=True)),
                ('investment', models.DecimalField(decimal_places=10, default=0, max_digits=19)),
                ('rate_time', models.IntegerField(default=0)),
                ('investor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.project')),
            ],
            options={
                'permissions': (('can_add_instance_proyect', 'Puede añadir inversión'),),
            },
        ),
    ]
