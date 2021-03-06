# Generated by Django 2.1.7 on 2019-03-11 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20190310_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
                ('is_answered', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Question')),
            ],
        ),
    ]
