# Generated by Django 2.1.1 on 2018-09-14 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=125)),
                ('merk', models.CharField(blank=True, max_length=30, null=True)),
                ('gambar', models.ImageField(blank=True, null=True, upload_to='')),
                ('harga', models.DecimalField(decimal_places=2, max_digits=15)),
                ('qty', models.IntegerField(blank=True, default=0)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produk.Kategori')),
            ],
        ),
    ]
