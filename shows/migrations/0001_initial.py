# Generated by Django 5.0.1 on 2024-01-19 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('network', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
            ],
        ),
    ]