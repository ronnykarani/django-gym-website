# Generated by Django 3.0.5 on 2021-12-31 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb', models.URLField()),
                ('twit', models.URLField()),
                ('insta', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Nav',
        ),
    ]
