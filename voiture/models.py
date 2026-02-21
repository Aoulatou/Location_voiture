from django.contrib.auth.hashers import make_password, check_password
from django.db import models
import random
import string
from django.utils import timezone
from datetime import timedelta


# ENUMS avec choices

class Role(models.TextChoices):
    CLIENT = "client", "Client"
    PROPRIETAIRE = "proprietaire", "Propriétaire"
    VÉRIFICATEUR = "veyra", "Vérificateur"

class Transmission(models.TextChoices):
    AUTOMATIQUE = "automatique", "Automatique"
    MANUELLE = "manuelle", "Manuelle"

class StatutReservation(models.TextChoices):
    EN_ATTENTE = "en_attente", "En attente"
    CONFIRMEE = "confirmee", "Confirmée"
    EN_COURS = "EN_COURS", "En cours"
    TERMINEE = "TERMINEE", "Terminée"
    ANNULEE = "annulee", "Annulée"

class MoyenPaiement(models.TextChoices):
    CARTE = "Carte", "Carte bancaire"
    PAYPAL = "PayPal", "PayPal"
    MOBILE_MONEY = "MobileMoney", "Mobile Money"

class StatutPaiement(models.TextChoices):
    EFFECTUE = "effectue", "Effectué"
    ECHOUE = "echoue", "Échoué"
    REMBOURSE = "rembourse", "Remboursé"



# MODELES

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CLIENT)
    password = models.CharField(max_length=128) 
    date_creation = models.DateTimeField(default=timezone.now, editable=False)
    is_active = models.BooleanField(default=True)
    
    # Champs pour vérification email à l'inscription
    email_verified = models.BooleanField(default=False)
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Hasher le mot de passe avant la sauvegarde
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.role})"

    # Génère un code OTP à 6 chiffres pour vérification email
    def generate_otp(self):
        import random
        self.otp_code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        self.otp_created_at = timezone.now()
        self.save()
        return self.otp_code
    
    # Vérifie si le code OTP est valide
    def verify_otp(self, code):
        if not self.otp_code or not self.otp_created_at:
            return False
        
        # Vérifier si le code correspond
        if self.otp_code != code:
            return False
        
        # Vérifier si le code n'a pas expiré (10 minutes)
        expiration_time = self.otp_created_at + timedelta(minutes=10)
        if timezone.now() > expiration_time:
            return False
        
         # Code valide, activer le compte
        self.email_verified = True
        self.is_active = True
        self.otp_code = None
        self.otp_created_at = None
        self.save()
        return True
    

class Voiture(models.Model):
    proprietaire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="voitures")
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee = models.PositiveIntegerField()
    couleur = models.CharField(max_length=30)
    immatriculation = models.CharField(max_length=50, unique=True)
    transmission = models.CharField(max_length=20, choices=Transmission.choices, default=Transmission.MANUELLE)
    nb_places = models.IntegerField()
    prix_jour = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilite = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="voitures/")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.immatriculation})"


class Reservation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="reservations")
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, related_name="reservations")
    dateDebut = models.DateField()
    dateFin = models.DateField()
    statutR = models.CharField(max_length=20, choices=StatutReservation.choices, default=StatutReservation.EN_ATTENTE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    numero = models.CharField(max_length=10, unique=True, editable=False, blank=True) 
    date_creation = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return f"Réservation {self.numero} {self.voiture} par {self.utilisateur} ({self.statutR})"
    
    @property
    def duree(self):
        #Calcule la durée en jours
        if self.dateDebut and self.dateFin:
            return (self.dateFin - self.dateDebut).days + 1
        return 0
    
    def save(self, *args, **kwargs):
        # Générer le numéro uniquement si c'est une nouvelle réservation
        if not self.numero:
            self.numero = self.generer_numero_unique()
        
        # Calculer automatiquement le montant si non défini
        if not self.montant and self.voiture:
            duree = (self.dateFin - self.dateDebut).days + 1
            self.montant = duree * self.voiture.prix_jour
        
        super().save(*args, **kwargs)
        self.gerer_disponibilite_voiture()
    
    def generer_numero_unique(self):
        #Génère un numéro de réservation unique
        while True:
            prefix = random.choice(string.ascii_uppercase)
            chiffres = str(random.randint(1000, 9999))
            numero = f"{prefix}{chiffres}"
            
            if not Reservation.objects.filter(numero=numero).exists():
                return numero
    
    #Gèrer la disponibilité de la voiture selon le statut
    def gerer_disponibilite_voiture(self):        
        if self.statutR in [StatutReservation.CONFIRMEE, StatutReservation.EN_ATTENTE, StatutReservation.EN_COURS]:
            self.voiture.disponibilite = False
            self.voiture.save()
        elif self.statutR in [StatutReservation.ANNULEE, StatutReservation.TERMINEE]:
            # Vérifier s'il n'y a pas d'autres réservations actives
            autres_reservations_actives = Reservation.objects.filter(
                voiture=self.voiture,
                statutR__in=[StatutReservation.CONFIRMEE, StatutReservation.EN_ATTENTE, StatutReservation.EN_COURS],
            ).exclude(id=self.id).exists()
            
            if not autres_reservations_actives:
                self.voiture.disponibilite = True
                self.voiture.save()


class Paiement(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, related_name="paiement")
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    datePaiement = models.DateTimeField(auto_now_add=True)
    moyenPaiement = models.CharField(max_length=20, choices=MoyenPaiement.choices)
    statutP = models.CharField(max_length=20, choices=StatutPaiement.choices, default=StatutPaiement.EFFECTUE)

    def __str__(self):
        return f"Paiement {self.montant} - {self.statutP}"


class Avis(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="avis")
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE, related_name="avis")
    note = models.PositiveSmallIntegerField()
    commentaire = models.TextField(blank=True, null=True)
    dateAvis = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avis {self.note}/5 de {self.utilisateur} sur {self.voiture}"
