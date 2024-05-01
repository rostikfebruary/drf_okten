# Generated by Django 5.0.4 on 2024-04-30 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=0)),
                ('seats', models.IntegerField(default=0)),
                ('body', models.CharField(max_length=50)),
                ('volume', models.FloatField(default=0)),
            ],
        ),
    ]