# Generated by Django 4.1.7 on 2023-03-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_request',
            name='extra_tickets',
            field=models.IntegerField(default=6),
            preserve_default=False,
        ),
    ]
