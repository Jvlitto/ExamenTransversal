# Generated by Django 4.0.5 on 2022-07-03 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appgestion', '0004_alter_persona_rut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=10)),
                ('laboratorio', models.CharField(max_length=10)),
                ('stock', models.IntegerField()),
                ('fecha_elab', models.CharField(max_length=30)),
                ('fecha_ven', models.CharField(max_length=30)),
            ],
        ),
    ]
