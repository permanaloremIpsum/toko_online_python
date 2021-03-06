# Generated by Django 2.1.1 on 2018-10-31 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0003_order_orderbarang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='alamat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='no_hp',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('cart', 'In Cart'), ('checkout', 'Checkout'), ('paid', 'Terbayar'), ('delivered', 'Terkirim')], default='cart', max_length=10),
        ),
        migrations.AlterField(
            model_name='orderbarang',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderbarangnya', to='produk.Order'),
        ),
        migrations.AlterField(
            model_name='orderbarang',
            name='produk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderbarangnya', to='produk.Produk'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='harga',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='produk',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='orderbarang',
            name='totalhargabarang',
        ),
        migrations.AlterUniqueTogether(
            name='orderbarang',
            unique_together={('order', 'produk')},
        ),
    ]
