# Generated by Django 4.0 on 2021-12-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_alter_profile_introduce_alter_profile_wpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='picprd',
            field=models.ImageField(null=True, upload_to='%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='work',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='%Y/%m/%d'),
        ),
    ]
