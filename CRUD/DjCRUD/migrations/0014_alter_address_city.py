# Generated by Django 4.1.1 on 2022-10-03 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjCRUD', '0013_alter_address_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=215, null=True),
        ),
    ]
