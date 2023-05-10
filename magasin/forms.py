from django.forms import ModelForm
from .models import Produit,Message,Fournisseur,Commande,Categorie
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ProduitForm(ModelForm): 
    class Meta : 
        model = Produit 
        fields = "__all__" #pour tous les champs de la table
#fields=['libelle','description'] #pour qulques champs
class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__"

class MessageForm(ModelForm):
     class Meta : 
        model = Message
        fields = "__all__" #pour tous les champs de la table
     


class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"
        widgets = {
            'produits': forms.CheckboxSelectMultiple()
        }

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__" 
