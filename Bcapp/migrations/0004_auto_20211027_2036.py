# Generated by Django 3.2 on 2021-10-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bcapp', '0003_bcmodel_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bcmodel',
            name='day',
        ),
        migrations.AddField(
            model_name='bcmodel',
            name='date',
            field=models.TextField(choices=[('Mon', '1'), ('Tue', '2'), ('Wed', '3'), ('Thu', '4'), ('Fri', '5'), ('M', '6'), ('o', '7'), ('a', '8'), ('b', '9'), ('c', '10'), ('d', '11'), ('e', '12'), ('f', '13'), ('g', '14'), ('h', '15'), ('i', '16'), ('sa', '17'), ('j', '18'), ('k', '19'), ('l', '20'), ('n', '21'), ('p', '22'), ('ao', '23'), ('adx', '24'), ('Mas', '25'), ('sa', '26'), ('on', '27'), ('Mn', '28'), ('asd', '29'), ('qw', '30'), ('xl', '31')], default='', max_length=10),
        ),
    ]
