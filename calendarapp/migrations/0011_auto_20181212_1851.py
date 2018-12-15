# Generated by Django 2.1.2 on 2018-12-12 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0010_auto_20181207_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='my_events',
            field=models.ManyToManyField(related_name='my_events', to='calendarapp.Event'),
        ),
        migrations.AddField(
            model_name='user',
            name='my_orgs',
            field=models.ManyToManyField(to='calendarapp.Organization'),
        ),
        migrations.AlterField(
            model_name='user',
            name='favorite_events',
            field=models.ManyToManyField(related_name='fav_events', to='calendarapp.Event'),
        ),
    ]