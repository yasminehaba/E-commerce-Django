from rest_framework.serializers import ModelSerializer
from .models import Categorie
from rest_framework import serializers
from .models import Produit

class ProduitSerializer(ModelSerializer):
    class Meta:
        model = Produit
        fields ='__all__'
class CategorySerializer(ModelSerializer):
 
    class Meta:
        model = Categorie
        fields = ['id', 'name']
