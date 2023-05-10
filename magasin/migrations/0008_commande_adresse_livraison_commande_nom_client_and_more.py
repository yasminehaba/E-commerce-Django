# Generated by Django 4.1.7 on 2023-05-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0007_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='adresse_livraison',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='commande',
            name='nom_client',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='commande',
            name='produits',
            field=models.ManyToManyField(related_name='produits', to='magasin.produit'),
        ),
    ]
