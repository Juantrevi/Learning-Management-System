# Generated by Django 5.0 on 2024-09-16 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_cartorderitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorderitem',
            name='coupons',
        ),
        migrations.AddField(
            model_name='cartorderitem',
            name='coupons',
            field=models.ManyToManyField(blank=True, to='api.coupon'),
        ),
    ]
