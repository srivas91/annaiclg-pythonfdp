# Generated by Django 4.2.1 on 2023-11-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("stuid", models.IntegerField(primary_key=True, serialize=False)),
                ("stuname", models.CharField(max_length=30)),
            ],
        ),
    ]
