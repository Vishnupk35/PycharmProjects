# Generated by Django 4.0.6 on 2022-08-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapi', '0005_alter_reviews_rating_alter_reviews_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('incart', 'incart'), ('order placed', 'order placed'), ('cancelled', 'cancelled')], default='incart', max_length=150),
        ),
    ]