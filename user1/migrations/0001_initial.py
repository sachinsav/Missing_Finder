# Generated by Django 3.0.2 on 2020-03-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=64)),
                ('mob_nu', models.IntegerField()),
                ('address', models.CharField(max_length=128)),
            ],
        ),
    ]
