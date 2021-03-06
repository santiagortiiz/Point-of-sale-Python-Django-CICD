# Generated by Django 3.1.14 on 2022-03-13 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('active', models.BooleanField(default=True, help_text='\n            Designates whether this user should be treated as active.\n            Unselect this instead of deleting accounts.\n        ', verbose_name='active or not')),
                ('total', models.PositiveIntegerField(default=0, help_text='Price in cents')),
            ],
            options={
                'db_table': 'orders',
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('active', models.BooleanField(default=True, help_text='\n            Designates whether this user should be treated as active.\n            Unselect this instead of deleting accounts.\n        ', verbose_name='active or not')),
                ('description', models.CharField(help_text='Description of the product at the time of purchase', max_length=255)),
                ('quantity', models.PositiveIntegerField(default=1, help_text='Requested units')),
                ('unit_price', models.PositiveIntegerField(default=0, help_text='unit price in cents', verbose_name='unit price')),
                ('total', models.PositiveIntegerField(default=0, help_text='formula: total = unit_price x quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.product')),
            ],
            options={
                'db_table': 'order_items',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='orders.OrderItem', to='inventory.Product'),
        ),
    ]
