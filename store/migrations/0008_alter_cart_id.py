# Generated by Django 5.0.6 on 2024-05-26 09:44

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_collection_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('af58785a-5ef1-49c5-80d1-32a329af96c0'), primary_key=True, serialize=False),
        ),
    ]
