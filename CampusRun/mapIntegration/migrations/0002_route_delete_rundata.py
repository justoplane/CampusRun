# Generated by Django 4.0.2 on 2022-03-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapIntegration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr1', models.TextField()),
                ('addr2', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='runData',
        ),
    ]
