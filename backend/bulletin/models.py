from django.db import models

# Create your models here.

class Personne(models.Model):
    matricule = models.CharField(max_length = 10)
    nom = models.CharField(max_length = 254)
    prenom = models.CharField(max_length = 254)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length = 254)
    nationalite = models.CharField(max_length = 254)
    email = models.EmailField()
    tel = models.CharField(max_length = 15)

    def __str__(self):
        return self.nom
