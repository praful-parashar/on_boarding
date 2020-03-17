# Generated by Django 2.2.4 on 2020-03-16 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_auto_20200305_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(related_name='tx_items', to='plan.Item')),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchant_transactions', to='plan.Merchant')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_transactions', to='plan.Store')),
            ],
        ),
    ]
