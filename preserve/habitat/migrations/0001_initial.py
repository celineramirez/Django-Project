# Generated by Django 5.1.2 on 2024-10-15 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('thumbnail', models.URLField()),
                ('history', models.TextField(null=True)),
                ('threats', models.TextField(null=True)),
                ('invasive_species', models.TextField(null=True)),
                ('conservation_strategies', models.TextField(null=True)),
            ],
        ),
    ]
