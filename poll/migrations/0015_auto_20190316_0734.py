# Generated by Django 2.1.7 on 2019-03-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0014_question_poll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='case',
        ),
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
