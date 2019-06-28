# Generated by Django 2.2.1 on 2019-06-09 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190523_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(0, 'Order Cancelled'), (1, 'Order Placed'), (2, 'Order Shipped'), (3, 'Order Delivered')], default=1),
        ),
    ]