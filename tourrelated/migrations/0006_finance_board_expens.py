# Generated by Django 2.0.13 on 2019-04-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourrelated', '0005_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='finance_board',
            name='expens',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]