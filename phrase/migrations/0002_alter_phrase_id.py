# Generated by Django 3.2.5 on 2021-07-31 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phrase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrase',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
