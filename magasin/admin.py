from django.contrib import admin
from.models import Produit,Categorie,Fournisseur,ProduitNC,Commande,Message
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Fournisseur)# pour enregistrer le novau table en admine 
admin.site.register(ProduitNC)
admin.site.register(Commande)
admin.site.register(Message)
# Register your models here.
