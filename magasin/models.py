from datetime import date

from django.db import models
from django.contrib.auth.models import User
class Address(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    locality = models.CharField(max_length=150, verbose_name="Nearest Location")
    city = models.CharField(max_length=150, verbose_name="City")
    state = models.CharField(max_length=150, verbose_name="State")

    def __str__(self):
        return self.locality
class Produit(models.Model):
    TYPE_CHOICES=[('em','emballé'),
              ('fr','frais'),
              ('cs','conservé')
              ]
    libellé = models.CharField(max_length=100)
    description = models.TextField(default='non definie')
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    type = models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)
    fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    img=models.ImageField(blank=True,upload_to='media/')
    def __str__(self):
        return (self.libellé +","+self.description+","+str(self.prix)+"," +self.type )

class Categorie(models.Model):
    TYPE_CHOICES=[('AL','Alimentaire'),
                  ('Mb','Meuble'),
                  ('Sn','Sanitaire'),
                  ('Vs','Vaisselle'),
                  ('Vt','Vêtement'),
                  ('Jx','Jouets'),
                  ('Lg','Linge de Maison'),
                  ('Bj','Bijoux'),
                  ('Dc','Décor')
                  ]
    name=models.CharField(max_length=50,default='AL',choices=TYPE_CHOICES)
    
    def __str__(self):
        return self.name
    
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100,null=True)
    adresse=models.TextField(null=True)
    email=models.EmailField(null=True)
    telephone=models.CharField(max_length=8,null=True)

    def __str__(self):
        return (self.nom+','+self.adresse+','+self.email+','+self.telephone)
    
class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return "objet ProduitNC:%s"%(self.Duree_garantie)

"""class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    
    def __str__(self):
        return"objet Produit :%s,%s"% (self.dateCde+','+self.totalCde)"""
    
class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    nom_client = models.CharField(max_length=100,default="")
    adresse_livraison = models.CharField(max_length=200,default="")
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField(Produit, related_name='produits')

    def __str__(self):
        return str(self.dateCde) + ' - ' + str(self.totalCde)

    def get_produits_info(self):
    
        return [(p.libellé, p.prix,p.qte) for p in self.produits.all()]

# python manage.py migrate
#python manage.py makemigrations


# Create your models here.




class Message(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.nom
class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, verbose_name="Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.user)
    
    # Creating Model Property to calculate Quantity x Price
    @property
    def total_price(self):
        return self.quantity * self.product.price


STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled')
)
class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    address = models.ForeignKey(Address, verbose_name="Shipping Address", on_delete=models.CASCADE)
    product = models.ForeignKey(Produit, verbose_name="Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="Ordered Date")
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=50,
        default="Pending"
        )


