# Generated by Django 4.2.7 on 2024-05-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_id',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
