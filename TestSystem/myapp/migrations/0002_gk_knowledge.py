# Generated by Django 3.2.5 on 2021-09-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GK_Knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sr_No', models.IntegerField()),
                ('Question', models.CharField(max_length=250)),
                ('Option_a', models.CharField(max_length=250)),
                ('Option_b', models.CharField(max_length=250)),
                ('Option_c', models.CharField(max_length=250)),
                ('Option_d', models.CharField(max_length=250)),
                ('Group', models.CharField(max_length=250)),
            ],
        ),
    ]
