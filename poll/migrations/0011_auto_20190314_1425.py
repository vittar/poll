# Generated by Django 2.1.7 on 2019-03-14 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0010_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='is_answered',
            field=models.IntegerField(default=0),
        ),
    ]
