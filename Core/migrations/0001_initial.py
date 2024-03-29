# Generated by Django 3.2.6 on 2021-08-18 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('uploadedFile', models.FileField(upload_to='uploaded_files/')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('version', models.CharField(max_length=200)),
                ('int_exch_id', models.CharField(max_length=200)),
                ('int_exch_name', models.CharField(max_length=200)),
            ],
        ),
    ]
