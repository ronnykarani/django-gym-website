# Generated by Django 3.0.5 on 2021-12-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_contact_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url1', models.URLField(null=True)),
                ('url2', models.URLField(null=True)),
            ],
        ),
    ]
