# Generated manually - Rename miliege to mileage

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalcars', '0003_carz_timestamps_rating_fix'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carz',
            old_name='miliege',
            new_name='mileage',
        ),
    ]
