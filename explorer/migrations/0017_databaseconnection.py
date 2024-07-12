# Generated by Django 5.0.4 on 2024-05-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0016_alter_explorervalue_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=255, unique=True)),
                ('engine', models.CharField(choices=[('django.db.backends.sqlite3', 'SQLite3'), ('django.db.backends.postgresql_psycopg2', 'PostgreSQL'), ('django.db.backends.mysql', 'MySQL'), ('django.db.backends.oracle', 'Oracle')], max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('user', models.CharField(blank=True, max_length=255)),
                ('password', models.CharField(blank=True, max_length=255)),
                ('host', models.CharField(blank=True, max_length=255)),
                ('port', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]