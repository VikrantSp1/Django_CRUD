# Generated by Django 4.1.1 on 2022-09-29 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjCRUD', '0005_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='postel_code',
            field=models.IntegerField(blank=True, max_length=215, null=True),
        ),
    ]