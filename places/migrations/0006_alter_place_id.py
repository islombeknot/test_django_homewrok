# Generated by Django 5.0.3 on 2024-03-31 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_placecomment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
