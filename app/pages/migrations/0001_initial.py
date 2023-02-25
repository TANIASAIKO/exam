# Generated by Django 4.1.7 on 2023-02-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(choices=[('Diamonds', 'Diamonds'), ('Hearts', 'Hearts'), ('Clubs', 'Clubs'), ('Spades', 'Spades')], default='Diamonds', max_length=10)),
                ('suit', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('Jack', 'Jack'), ('Queen', 'Queen'), ('King', 'King'), ('Ace', 'Ace'), ('Joker', 'Joker')], default='2', max_length=8)),
                ('icon', models.CharField(choices=[('diamond', 'diamond'), ('favorite', 'favorite'), ('spa', 'spa'), ('eco', 'eco')], default='diamond', max_length=10)),
            ],
        ),
    ]
