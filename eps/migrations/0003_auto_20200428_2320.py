# Generated by Django 2.2 on 2020-04-29 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eps', '0002_auto_20200412_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenmedica',
            name='medicamentos',
            field=models.ManyToManyField(blank=True, to='medicamentos.Medicamento'),
        ),
    ]
