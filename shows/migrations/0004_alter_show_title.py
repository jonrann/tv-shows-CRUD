# Generated by Django 5.0.1 on 2024-01-20 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_alter_show_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
