# Generated by Django 3.2.5 on 2021-07-08 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='html',
            field=models.TextField(default=''),
        ),
    ]