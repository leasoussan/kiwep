

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210608_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='city',
        ),
    ]
