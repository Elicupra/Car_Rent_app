# Generated manually - Adding timestamps and fixing rating

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rentalcars', '0002_carz_miliege'),
    ]

    operations = [
        migrations.AddField(
            model_name='carz',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carz',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='carz',
            name='category',
            field=models.CharField(choices=[('SUV', 'SUV'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Minivan', 'Minivan'), ('Pickup Truck', 'Pickup Truck')], default='Sedan', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carz',
            name='price_per_day',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carz',
            name='is_available',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carz',
            name='rating',
            field=models.DecimalField(decimal_places=1, help_text='Rating out of 5.0', max_digits=3),
        ),
    ]
