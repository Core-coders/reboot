# Generated by Django 2.2.5 on 2020-02-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hmdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hmname', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Studentdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bloodgroup', models.CharField(max_length=100)),
                ('dob', models.DateTimeField()),
                ('aadhar', models.IntegerField()),
            ],
        ),
    ]