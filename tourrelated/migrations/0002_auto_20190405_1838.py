# Generated by Django 2.0.13 on 2019-04-05 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourrelated', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member_on_tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=200)),
                ('p_money', models.CharField(max_length=10)),
                ('due', models.CharField(max_length=10)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourrelated.Tour')),
            ],
        ),
        migrations.RemoveField(
            model_name='add_member_on_tour',
            name='tour',
        ),
        migrations.DeleteModel(
            name='Add_member_on_tour',
        ),
    ]
