# Generated by Django 4.0.3 on 2022-03-06 09:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoingateOrder',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price_amount', models.FloatField()),
                ('price_currency', models.CharField(max_length=10)),
                ('receive_currency', models.CharField(max_length=10)),
                ('coingate_order_id', models.PositiveIntegerField(unique=True)),
                ('receive_amount', models.FloatField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('callback_url', models.URLField(blank=True, null=True)),
                ('cancel_url', models.URLField(blank=True, null=True)),
                ('success_url', models.URLField(blank=True, null=True)),
                ('token', models.CharField(blank=True, max_length=200, null=True)),
                ('purchaser_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
