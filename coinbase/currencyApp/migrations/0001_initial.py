# Generated by Django 4.0.3 on 2022-03-05 17:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price_amount', models.FloatField()),
                ('price_currency', models.FloatField()),
                ('receive_currency', models.FloatField()),
                ('receive_amount', models.FloatField()),
            ],
        ),
    ]
