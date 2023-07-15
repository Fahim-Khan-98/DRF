# Generated by Django 3.2.19 on 2023-06-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('it', 'IT'), ('brac', 'Brac'), ('housing', 'Housing')], max_length=200)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]