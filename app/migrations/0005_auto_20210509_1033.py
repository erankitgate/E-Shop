# Generated by Django 2.2.14 on 2021-05-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_orders'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='id',
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
