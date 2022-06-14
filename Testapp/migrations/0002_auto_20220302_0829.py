# Generated by Django 3.2.12 on 2022-03-02 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dist',
            field=models.CharField(default=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default=False, max_length=13),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profession',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
