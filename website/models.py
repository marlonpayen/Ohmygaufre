'''
Created on 11 Jan 2024

@author: mpayen
'''
'''
Created on 11 Jan 2024

@author: mpayen
'''
from django.db import models
from django.core.exceptions import ValidationError
    

class Foodtruck(models.Model):
    nom = models.CharField(max_length=50)
    ville = models.CharField(max_length=20)
    adresse = models.TextField()
    numero_de_telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    heure_d_ouverture = models.CharField(max_length=10)
    heure_de_fermeture = models.CharField(max_length=10)
    a_propos = models.TextField() # Bigger than CharField object and text area rendered on the HTML file
    phrase_d_accroche = models.TextField() # Bigger than CharField object and text area rendered on the HTML file
    proprietaires = models.TextField() # Bigger than CharField object and text area rendered on the HTML file
    image_accueil = models.ImageField(upload_to='') # Upload of the profile image in the media folder (defined in MEDIA_ROOT)
    image_du_menu = models.ImageField(upload_to='') # Upload of the profile image in the media folder (defined in MEDIA_ROOT)
    
    '''cree_a = models.DateTimeField(auto_now_add=True)
    modifie_a = models.DateTimeField(auto_now=True)'''
    
    # We can only have one profile, the owner of the food truck
    def clean(self):
        if Foodtruck.objects.exists() and not self.pk:
            raise ValidationError("Il ne peut y avoir qu'un seul foodtruck")
    
    
    def save(self, *args, **kwargs):
        return super(Foodtruck, self).save(*args, **kwargs) #saves the record
        
        
class Message(models.Model):
    date_de_publication = models.DateTimeField()
    nom = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    sujet = models.CharField(max_length=100)
    contenu = models.TextField()
    
    
class Menu(models.Model):
    nom = models.CharField(max_length=50)
    
    
class MenuItem(models.Model):
    nom = models.CharField(max_length=70)
    description = models.TextField()
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name= 'menuitems')
            
            
