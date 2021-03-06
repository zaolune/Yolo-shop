# Generated by Django 3.2.4 on 2022-02-11 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0004_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menthod', models.CharField(blank=True, choices=[('alipay', 'alipay'), ('weixinpay', 'weixinpay')], max_length=32, null=True)),
                ('out_trade_no', models.CharField(max_length=64, unique=True)),
                ('trade_no', models.CharField(blank=True, max_length=64, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]
