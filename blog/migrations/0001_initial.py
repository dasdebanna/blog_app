# Generated by Django 4.2.1 on 2023-06-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]
