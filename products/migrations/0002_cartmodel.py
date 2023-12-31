# Generated by Django 4.2.4 on 2023-08-31 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.productsmodel')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.categoriesmodel')),
            ],
        ),
    ]
