# Generated by Django 3.2.5 on 2021-09-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client1',
            name='Phone',
            field=models.IntegerField(max_length=250),
        ),
    ]
