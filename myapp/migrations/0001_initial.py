# Generated by Django 5.0.2 on 2024-02-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Class', models.CharField(max_length=50)),
                ('Section', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
            ],
        ),
    ]