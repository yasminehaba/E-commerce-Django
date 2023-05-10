from django.urls import include, path 
from . import views
from .views import CategoryAPIView
from .views import ProduitAPIView
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView
from django.contrib.auth.views import LoginView
from . import views

# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('produit', ProductViewset, basename='produit')

urlpatterns = [
    
    #  path('message/', views.message, name='message'),
    #  path('TtMessage/', views.TtMessage, name='TtMessage'),
    #  path('deleteMessage/<int:pk>/', views.delete_message, name='delete_message'),
    #  path('Message/<int:msg_id>/', views.detail_message, name='detail_message'),
    
    path('', views.index, name='index'),
    path('indexA', views.indexA, name='indexA'),
    path('home/', views.indexA, name='home'),
   
    path('ListCategorie/', views.ListCategorie, name='ListCategorie'),
    path('create_categorie/',views.create_categorie,name='create_categorie'),
    path('editCategorie/<int:pk>/', views.edit_categorie, name='edit_categorie'),
    path('deleteCategorie/<int:pk>/', views.delete_categorie, name='delete_categorie'),
    path('Categorie/<int:categorie_id>/', views.detail_categorie, name='detail_categorie'),
    path('produits/', views.Produit_index, name='produits'),
    #path('',views.home,name='home'),
    #path('categories/', views.Categorie_index, name='categories'),
    #path('fournisseurs/', views.Fournisseur_index, name='fournisseurs'),
    path('fournisseurs/', views.ListFournisseur, name='fournisseurs'),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouvFournisseur'),
    path('editFournisseur/<int:fk>/', views.edit_Fournisseur, name='edit_Fournisseur'),
    path('deleteFournisseur/<int:fk>/', views.delete_Fournisseur, name='delete_Fournisseur'),
    path('Fournisseur/<int:for_id>/', views.detail_Fournisseur, name='detail_Fournisseur'),

    path('ListCommande/', views.ListCommande, name='ListCommande'),
    path('create_commande/',views.create_commande,name='create_commande'),
     path('editCommande/<int:pk>/', views.edit_commande, name='edit_commande'),
    path('deleteCommande/<int:pk>/', views.delete_commande, name='delete_commande'),
    path('Commande/<int:commande_id>/', views.detail_commande, name='detail_commande'),

    path('maj-produits/', views.ProduitF_index, name='produit_form'),
    path('register/',views.register, name = 'register'),
    path('supprimer_produit/<int:id>/',views. supprimer_produit, name='supprimer_produit'),           path('modifier_produit/<int:id>/',views. modifier_produit, name='modifier_produit'),
    path('modifier_produit/<int:id>/',views. modifier_produit, name='modifier_produit'), 
    
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    #path('api/', inpyclude(router.urls)),

    path('message/', views.message, name='message'),
    path('TtMessage/', views.TtMessage, name='TtMessage'),
    path('deleteMessage/<int:pk>/', views.delete_message, name='delete_message'),
    path('Message/<int:msg_id>/', views.detail_message, name='detail_message'),
    
]
