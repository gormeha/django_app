# Generated by Django 2.2.1 on 2019-05-20 02:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(0, 'Order Cancelled'), (1, 'Order Placed'), (2, 'Order Shipped'), (3, 'Order Delivered')], default=1, max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='interested_in',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='warehouse',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='num_units',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
