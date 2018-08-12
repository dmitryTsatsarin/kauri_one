# Generated by Django 2.0.7 on 2018-08-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketNormalizedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency', models.CharField(choices=[('BTC', 'BITCOIN'), ('ETH', 'ETHEREUM'), ('XRP', 'RIPPLE')], max_length=255)),
                ('to_currency', models.CharField(choices=[('BTC', 'BITCOIN'), ('ETH', 'ETHEREUM'), ('XRP', 'RIPPLE')], max_length=255)),
                ('high_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('low_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('last_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('bid_datetime', models.DateTimeField()),
                ('market', models.CharField(choices=[('Binance', 'BINANCE'), ('HitBtc', 'HITBTC')], max_length=255)),
            ],
        ),
    ]