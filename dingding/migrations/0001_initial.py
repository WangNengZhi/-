# Generated by Django 2.2.1 on 2021-01-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DingTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=30, null=True)),
                ('remark', models.CharField(blank=True, max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ding_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('remark', models.CharField(blank=True, max_length=50, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('db_name', models.CharField(max_length=64)),
                ('path', models.CharField(max_length=65)),
            ],
            options={
                'db_table': 'url',
                'managed': False,
            },
        ),
    ]
