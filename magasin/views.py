
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Produit
from .models import Categorie,Message
from .models import Fournisseur
from .models import Commande
from .forms import ProduitForm ,FournisseurForm,UserRegistrationForm,MessageForm,UserCreationForm,CommandeForm,CategorieForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from magasin.serializers import CategorySerializer
from rest_framework.generics import ListAPIView
from .models import Produit
from .serializers import ProduitSerializer
from rest_framework import viewsets
from django.shortcuts import render
from django.shortcuts import render


from rest_framework import viewsets

# def TtMessage(request):
#         messages= Message.objects.all()
#         context={'messages':messages}
#         return render( request,'messages/messages.html',context )

# def message(request):
#        if request.method == "POST" :
#          form = MessageForm(request.POST,request.FILES)
#          if form.is_valid():
#               form.save() 
#               messages=Message.objects.all()
              
#               return redirect('indexA')
#        else : 
#             form = MessageForm() #créer formulaire vide 
#             messages=Message.objects.all()
#             return render(request,'messages/create_msg.html',{'form':form,'messages':messages})
# def delete_message(request, pk):
#     msg = get_object_or_404(Message, pk=pk)
#     if request.method == 'POST':
#         msg.delete()
#         return redirect('TtMessage')
#     return render(request, 'messages/delete_msg.html', {'msg': msg})

# def detail_message(request, msg_id):
#     message = get_object_or_404(Message, id=msg_id)
#     context = {'message': message}
#     return render(request, 'messages/detail_msg.html', context)


class ProductViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = Produit.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

class ProduitAPIView(APIView):
    def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)


class CategoryAPIView(APIView):
 
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)



def indexA(request):
     return render(request,'magasin/home.html' )

from django.shortcuts import render

def index(request):
    if request.user.is_authenticated:
        request.session['username'] = request.user.username
    return render(request, 'index.html')

def index(request):
    list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list})
def Produit_index(request):
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/mesProduits.html', context)


def ProduitV_index(request):
    list = Produit.objects.all()
    return render(request, 'magasin/vitrine.html', {'list': list})

def ProduitF_index(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = ProduitForm()  # créer formulaire vide
    list =Produit.objects.all()
    return render(request, 'magasin/majProduits.html', {'form': form,'list':list})


"""def Categorie_index(request):
    categories = Categorie.objects.all()
    context = {'categories': categories}
    return render(request, 'magasin/mesCategories.html', context)"""

def ListFournisseur(request):
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs': fournisseurs}
    return render(request, 'magasin/Fournisseurs/mesFournisseurs.html', context)

def nouveauFournisseur(request):
    if request.method == "POST" :
         form = FournisseurForm(request.POST,request.FILES)
         if form.is_valid():
               # Récupérer l'instance du modèle produit
            frns = form.save(commit=False)
            # Récupérer la nouvelle image téléchargée
            nouvelle_image = form.cleaned_data['logo']
            # Si une nouvelle image a été téléchargée, la sauvegarder
            if nouvelle_image:
                frns.logo= nouvelle_image
            # Sauvegarder le produit
            form.save() 
            fournisseurs=Fournisseur.objects.all()
            return render(request,'magasin/Fournisseurs/mesFournisseurs.html',{'fournisseurs':fournisseurs})
    else : 
            form = FournisseurForm() #créer formulaire vide 
            fournisseurs=Fournisseur.objects.all()
            return render(request,'magasin/Fournisseurs/create_For.html',{'form':form,'fournisseurs':fournisseurs})

"""def Fournisseur_index(request):
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs': fournisseurs}
    return render(request, 'magasin/mesFournisseurs.html', context)
    if request.method == "POST" :
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = FournisseurForm() #créer formulaire vide
    return render(request,'magasin/mesFournisseurs.html',{'form':form})"""
def edit_Fournisseur(request, fk):
    fournisseur = get_object_or_404(Fournisseur, id=fk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, request.FILES, instance=fournisseur)
        if form.is_valid():
            # Récupérer l'instance du modèle produit
            frns = form.save(commit=False)
            # Récupérer la nouvelle image téléchargée
            nouvelle_image = form.cleaned_data['logo']
            # Si une nouvelle image a été téléchargée, la sauvegarder
            if nouvelle_image:
                frns.logo= nouvelle_image
            # Sauvegarder le produit
            frns.save()
            return redirect('fournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)
        return render(request, 'magasin/Fournisseurs/edit_For.html', {'form': form})

def delete_Fournisseur(request, fk):
    fournisseur = get_object_or_404(Fournisseur, id=fk)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('fournisseurs')
    return render(request,'magasin/Fournisseurs/delete_For.html', {'fournisseur': fournisseur})

def detail_Fournisseur(request, for_id):
    fournisseur = get_object_or_404(Fournisseur, id=for_id)
    context = {'fournisseur': fournisseur}
    return render(request, 'magasin/Fournisseurs/detail_For.html', context)

def create_commande(request):
       if request.method == "POST" :
         form = CommandeForm(request.POST)
         if form.is_valid():
              form.save() 
              commandes=Commande.objects.all()
              
              return render(request,'magasin/Commandes/mesCommandes.html',{'commandes':commandes})
       else : 
            form = CommandeForm() #créer formulaire vide 
            commandes=Commande.objects.all()
            return render(request,'magasin/Commandes/create_commande.html',{'form':form,'commandes':commandes})

def edit_commande(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('ListCommande')
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'magasin/Commandes/edit_commande.html', {'form': form})

def delete_commande(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('ListCommande')
    return render(request, 'magasin/Commandes/delete_commande.html', {'commande': commande})

def detail_commande(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    context = {'commande': commande}
    return render(request, 'magasin/Commandes/detail_commande.html', context)

def ListCommande(request):
        commandes= Commande.objects.all()
        context={'commandes':commandes}
        return render( request,'magasin/Commandes/mesCommandes.html',context )

from django.shortcuts import redirect, render, get_object_or_404


def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})
def modifier_produit(request, id):
    produit = Produit.objects.get(id=id)
    if request.method == "POST" :
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm(instance=produit)
    return render(request,'magasin/majProduits.html',{'form':form})

def supprimer_produit(request, id):
    produit = Produit.objects.get(id=id)
    produit.delete()
    return HttpResponseRedirect('/magasin')



def create_categorie(request):
       if request.method == "POST" :
         form = CategorieForm(request.POST)
         if form.is_valid():
              form.save() 
              categories=Categorie.objects.all()
              
              return render(request,'magasin/Categories/mesCategories.html',{'categories':categories})
       else : 
            form = CategorieForm() #créer formulaire vide 
            categories=Categorie.objects.all()
            return render(request,'magasin/Categories/create_categorie.html',{'form':form,'categories':categories})

def edit_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            categorie.save()
            return redirect('ListCategorie')
    else:
        form = CategorieForm(instance=categorie)
        return render(request, 'magasin/Categories/edit_categorie.html', {'form': form})

def delete_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('ListCategorie')
    return render(request, 'magasin/Categories/delete_categorie.html', {'categorie': categorie})

def detail_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)
    context = {'categorie': categorie}
    return render(request, 'magasin/Categories/detail_categorie.html', context)

def ListCategorie(request):
        categories= Categorie.objects.all()
        context={'categories':categories}
        return render( request,'magasin/Categories/mesCategories.html',context )



def TtMessage(request):
        messages= Message.objects.all()
        context={'messages':messages}
        return render( request,'messages/messages.html',context )

def message(request):
       if request.method == "POST" :
         form = MessageForm(request.POST,request.FILES)
         if form.is_valid():
              form.save() 
              messages=Message.objects.all()
              
              return redirect('indexA')
       else : 
            form = MessageForm() #créer formulaire vide 
            messages=Message.objects.all()
            return render(request,'messages/create_msg.html',{'form':form,'messages':messages})
def delete_message(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        msg.delete()
        return redirect('TtMessage')
    return render(request, 'messages/delete_msg.html', {'msg': msg})

def detail_message(request, msg_id):
    message = get_object_or_404(Message, id=msg_id)
    context = {'message': message}
    return render(request, 'messages/detail_msg.html', context)
