from django.shortcuts import render, redirect, get_object_or_404
from .utils import get_current_user, is_user_authenticated, login_user, logout_user
from django.contrib.auth.decorators import login_required
from .models import Utilisateur, Voiture, Reservation, Paiement, Avis
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils import timezone
from datetime import datetime


# ============================================================================================================
# CONNEXION DECONNEXION
# ============================================================================================================
# Connexion
def connexion(request):
    if is_user_authenticated(request):
        return redirect("Veyra")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if not email or not password:
            messages.error(request, "Veuillez remplir tous les champs")
            return render(request, "auth/connexion.html")
        
        try:
            user = Utilisateur.objects.get(email=email, is_active=True)
            if user.check_password(password):
                login_user(request, user)
                messages.success(request, f"Bienvenue  {user.nom} {user.prenom} !")
                return redirect("Veyra")  
            else:
                messages.error(request, "Mot de passe incorrect.")

        except Utilisateur.DoesNotExist:
            messages.error(request, "Aucun compte actif trouvé avec cet email.")

    return render(request, "auth/connexion.html")


# Déconnexion
def deconnexion(request):
    if is_user_authenticated(request):
        logout_user(request)
        messages.info(request, "Vous êtes déconnecté.")
    return redirect("Veyra")  


# ============================================================================================================
# Inscription Profil
# ============================================================================================================
# # Inscription
def inscription(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
        adresse = request.POST.get("adresse")
        role = request.POST.get("role") or "CLIENT"
        password = request.POST.get("password")
        password_confirm = request.POST.get("password")

        # Vérification des mots de passe
        if password != password_confirm:
            messages.error(request, "Le mot de passe ne correspondent pas.")
            return render(request, "auth/inscription.html")
        
        # if len(password) < 8:
        #     messages.error(request, 'Le mot de passe doit contenir au moins 8 caractères')
        #     return render(request, 'auth/inscription.html')
    
        # Vérification si l'email existe déjà
        if Utilisateur.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return render(request, "auth/inscription.html")

        # Création de l'utilisateur
        try: 
            user = Utilisateur(
            nom=nom,
            prenom=prenom,
            email=email,
            telephone=telephone,
            adresse=adresse,
            password=password,
            role=role
            )
            user.save()
            login_user(request, user)
            messages.success(request, "Inscription réussie ! Vous pouvez maintenant vous connecter.")
            return redirect("Veyra")

        except Exception as e:
            messages.error(request, 'Erreur lors de la création du compte. Veuillez réessayer.')
    
    return render(request, "auth/inscription.html")

# Profil

def profil(request):
    #Vue pour afficher et modifier le profil utilisateur
    if request.method == "POST":
        # Mise à jour du profil
        request.user.nom = request.POST.get("nom", request.user.nom)
        request.user.prenom = request.POST.get("prenom", request.user.prenom)
        request.user.telephone = request.POST.get("telephone", request.user.telephone)
        request.user.adresse = request.POST.get("adresse", request.user.adresse)
        
        # Gestion de la photo de profil
        if request.FILES.get("photo"):
            request.user.photo = request.FILES.get("photo")
        
        request.user.save()
        messages.success(request, "Profil mis à jour avec succès !")
        return redirect("profil")
    
    return render(request, "dashboard/profil.html", {"utilisateur": request.user})


# ============================================================================================================
# Dashboard
# ============================================================================================================
# Acceuil
def accueil(request):
    query = request.GET.get("q", "")
    voitures = Voiture.objects.all()

    if query:
        voitures = voitures.filter(
            Q(marque__icontains=query) |
            Q(modele__icontains=query) |
            Q(couleur__icontains=query) |
            Q(immatriculation__icontains=query)
        )

    # Compter les réservations actives pour l'utilisateur connecté
    reservations_actives_count = 0
    current_user = get_current_user(request)
    
    if current_user:
        reservations_actives_count = Reservation.objects.filter(
            utilisateur=current_user,
            statutR__in=['EN_ATTENTE', 'CONFIRMEE', 'ANNULEE']
        ).count()
    
    context = {
        'voitures': voitures,
        'reservations_actives_count': reservations_actives_count,
        'query': query
    }

    return render(request, "dashboard/accueil.html", context)




# ============================================================================================================
# UTILISATEURS
# ============================================================================================================
# vues pour la liste des utilisateurs
def liste_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    
    search = request.GET.get("search", "")
    if search:
        utilisateurs = utilisateurs.filter(
            Q(nom__icontains=search) |
            Q(prenom__icontains=search) |
            Q(email__icontains=search)
        )
    role = request.GET.get('role', '')
    if role:
        utilisateurs = utilisateurs.filter(role=role)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(utilisateurs, 5)
    page_obj = paginator.get_page(page_number)
    return render(request, "utilisateurs/liste.html", {"utilisateurs": page_obj,"search": search, "role": role})

# vues pour l'ajout des utilisateurs
def ajouter_utilisateurs(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
        adresse = request.POST.get("adresse")
        role = request.POST.get("role")
        password  = request.POST.get("pwd")

        # Vérifie que tous les champs sont présents
        if nom and prenom and email and telephone and adresse and role and password :
            # Création de l'utilisateur
            utilisateur = Utilisateur(
                nom=nom,
                prenom=prenom,
                email=email,
                telephone=telephone,
                adresse=adresse,
                role=role
            )
            utilisateur.pwd = password 
            utilisateur.save()
            messages.success(request, "Utilisateur ajouté avec succès ")
            return redirect('liste_utilisateurs')
        else:
            return render(request, 'utilisateurs/ajouter.html', {'error': 'Tous les champs sont requis'})
    return render(request, 'utilisateurs/ajouter.html')

# vues pour modifier des employées
def modifier_utilisateurs(request, id) :
    utilisateur = get_object_or_404(Utilisateur, id=id)

    if request.method == "POST":
        utilisateur.nom = request.POST.get("nom")
        utilisateur.prenom = request.POST.get("prenom")
        utilisateur.email = request.POST.get("email")
        utilisateur.telephone = request.POST.get("telephone")
        utilisateur.adresse = request.POST.get("adresse")
        utilisateur.role = request.POST.get("role")
        password = request.POST.get("pwd")
        if password:
            utilisateur.pwd = password

        utilisateur.save()
        messages.success(request, "Utilisateur modifié avec succès ")
        return redirect('liste_utilisateurs')
    return render(request, 'utilisateurs/modifier.html', {'utilisateur': utilisateur})

# vues pour supprimer des employées
def supprimer_utilisateurs(request, id) :
    utilisateur = get_object_or_404(Utilisateur, id=id)
    if request.method == 'POST' :
        utilisateur.delete()
        messages.success(request, "Utilisateur supprimé avec succès ")
        return redirect ('liste_utilisateurs')
    return render(request, 'utilisateurs/suppresion.html', {'utilisateur' : utilisateur})



# ============================================================================================================
# VOITURES
# ============================================================================================================
# Liste des voitures
def liste_voitures(request):
    voitures = Voiture.objects.all()
    
    search = request.GET.get("search", "")
    if search:
        voitures = voitures.filter(
            Q(marque__icontains=search) |
            Q(modele__icontains=search) |
            Q(annee__icontains=search) |
            Q(couleur__icontains=search) |
            Q(immatriculation__icontains=search)
        )
    role = request.GET.get('disponible')
    if role:
        voitures = voitures.filter(disponible=(role == '1'))

    page_number = request.GET.get('page', 1)
    paginator = Paginator(voitures, 5)
    page_obj = paginator.get_page(page_number)
    
    return render(request, "voitures/liste.html", {"voitures": page_obj,"search": search, "role": role})

# Ajouter une voiture
def ajouter_voitures(request):
    if request.method == "POST":
        proprietaire_id = request.POST.get("proprietaire")
        marque = request.POST.get("marque")
        modele = request.POST.get("modele")
        annee = request.POST.get("annee")
        couleur = request.POST.get("couleur")
        immatriculation = request.POST.get("immatriculation")
        nb_places = request.POST.get("nb_places")
        transmission = request.POST.get("transmission")
        prix_jour = request.POST.get("prix_jour")
        disponibilite = True if request.POST.get("disponibilite") == "on" else False
        photo = request.FILES.get("photo")
        description = request.POST.get("description")
        
        proprietaire = Utilisateur.objects.get(id=proprietaire_id, role='proprietaire')
        voiture = Voiture(
            proprietaire=proprietaire,
            marque=marque,
            modele=modele,
            annee=annee,
            couleur=couleur,
            immatriculation=immatriculation,
            transmission=transmission,
            nb_places=nb_places,
            prix_jour=prix_jour,
            disponibilite=disponibilite,
            photo=photo,
            description=description 
        )
        voiture.save()
        messages.success(request, "Voiture ajoutée avec succès ")
        return redirect("liste_voitures")

    utilisateurs = Utilisateur.objects.filter(role='proprietaire')

    return render(request, "voitures/ajouter.html", { "utilisateurs": utilisateurs })

# Modifier une voiture
def modifier_voitures(request, id):
    voiture = get_object_or_404(Voiture, id=id)
    utilisateurs = Utilisateur.objects.filter(role='proprietaire')

    if request.method == "POST":
        proprietaire_id = request.POST.get("proprietaire")
        voiture.proprietaire = Utilisateur.objects.get(id=proprietaire_id)
        voiture.marque = request.POST.get("marque")
        voiture.modele = request.POST.get("modele")
        voiture.annee = request.POST.get("annee")
        voiture.couleur = request.POST.get("couleur")
        voiture.immatriculation = request.POST.get("immatriculation")
        voiture.transmission = request.POST.get("transmission")
        voiture.nb_places = request.POST.get("nb_places")
        voiture.prix_jour = request.POST.get("prix_jour")
        voiture.disponibilite = True if request.POST.get("disponibilite") == "on" else False
        photo = request.FILES.get("photo")
        voiture.description  = request.POST.get("description")

        if photo:
            voiture.photo = photo

        voiture.save()
        messages.success(request, "Voiture modifiée avec succès ")
        return redirect("liste_voitures")

    return render(request, "voitures/modifier.html", {"voiture": voiture, "utilisateurs": utilisateurs})

# Supprimer une voiture
def supprimer_voitures(request, id):
    voiture = get_object_or_404(Voiture, id=id)
    if request.method == "POST":
        voiture.delete()
        messages.success(request, "Voiture supprimée avec succès ")
        return redirect("liste_voitures")
    return render(request, "voitures/suppression.html", {"voiture": voiture})



# ============================================================================================================
# RESERVATION
# ============================================================================================================
# Liste des réservation
def liste_reservations(request):
    reservations = Reservation.objects.all()
    
    search = request.GET.get("search", "")
    if search:
        reservations = reservations.filter(
            Q(numero__icontains=search) |
            Q(utilisateur__nom__icontains=search) |
            Q(utilisateur__prenom__icontains=search) |
            Q(voiture__marque__icontains=search) |
            Q(voiture__modele__icontains=search)
        )
    statutR = request.GET.get('statutR', '')
    if statutR:
        reservations = reservations.filter(statutR=statutR)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(reservations, 5)
    page_obj = paginator.get_page(page_number)
    
    return render(request, "reservations/liste.html", {"reservations": page_obj,"search": search, "statutR": statutR})

# Ajouter une réservation
def ajouter_reservations(request):
    utilisateurs = Utilisateur.objects.filter(role='CLIENT')
    voitures = Voiture.objects.filter(disponibilite=True)

    if request.method == "POST":
        utilisateur_id = request.POST.get("utilisateur")
        voiture_id = request.POST.get("voiture")
        dateDebut_str = request.POST.get("dateDebut")
        dateFin_str = request.POST.get("dateFin")
        statutR = request.POST.get("statutR")

        try:
            dateDebut = datetime.strptime(dateDebut_str, "%Y-%m-%d").date()
            dateFin = datetime.strptime(dateFin_str, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Format de date invalide.")
            return render(request, "reservations/ajouter.html", {"utilisateurs": utilisateurs, "voitures": voitures})

        # Validations
        if dateDebut < timezone.now().date():
            messages.error(request, "La date de début doit être >= à aujourd'hui.")
            return render(request, "reservations/ajouter.html", {"utilisateurs": utilisateurs, "voitures": voitures})
        
        if dateFin < dateDebut:
            messages.error(request, "La date de fin doit être >= à la date de début.")
            return render(request, "reservations/ajouter.html", {"utilisateurs": utilisateurs, "voitures": voitures})

        try:
            utilisateur = Utilisateur.objects.get(id=utilisateur_id)
            voiture = Voiture.objects.get(id=voiture_id)
            
            # Vérifier les chevauchements
            chevauchement = Reservation.objects.filter(
                voiture=voiture,
                statutR__in=['EN_ATTENTE', 'CONFIRMEE', 'ANNULEE'],
                dateDebut__lte=dateFin,
                dateFin__gte=dateDebut
            ).exists()
            
            if chevauchement:
                messages.error(request, "Cette voiture est déjà réservée pour cette période.")
                return render(request, "reservations/ajouter.html", {"utilisateurs": utilisateurs, "voitures": voitures})
            
            # Calcul du montant
            nb_jours = (dateFin - dateDebut).days + 1
            montant = nb_jours * voiture.prix_jour
            
            reservation = Reservation(
                utilisateur=utilisateur,
                voiture=voiture,
                dateDebut=dateDebut,
                dateFin=dateFin,
                statutR=statutR,
                montant=montant
            )
        
            messages.success(request, f"Réservation {reservation.numero} ajoutée avec succès")
            return redirect("liste_reservations")
        
        except (Utilisateur.DoesNotExist, Voiture.DoesNotExist) as e:
            messages.error(request, "Utilisateur ou voiture introuvable.")
            return render(request, "reservations/ajouter.html", {"utilisateurs": utilisateurs, "voitures": voitures})
    
    return render(request, "reservations/ajouter.html", {"utilisateurs": utilisateurs, "voitures": voitures})

# Modifier une réservation
def modifier_reservations(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    utilisateurs = Utilisateur.objects.filter(role='CLIENT')
    voitures = Voiture.objects.filter(disponibilite=True) | Voiture.objects.filter(id=reservation.voiture.id)

    if request.method == "POST":
        utilisateur_id = request.POST.get("utilisateur")
        voiture_id = request.POST.get("voiture")
        dateDebut_str = request.POST.get("dateDebut")
        dateFin_str = request.POST.get("dateFin")
        statutR = request.POST.get("statutR")

        # Conversion des dates
        try:
            dateDebut = datetime.strptime(dateDebut_str, "%Y-%m-%d").date()
            dateFin = datetime.strptime(dateFin_str, "%Y-%m-%d").date()
        except ValueError:
            messages.error(request, "Format de date invalide.")
            return render(request, "reservations/modifier.html", {"reservation": reservation, "utilisateurs": utilisateurs, "voitures": voitures})

        # Validation: dates
        if dateDebut < timezone.now().date():
            messages.error(request, "La date de début doit être >= aujourd’hui.")
            return render(request, "reservations/modifier.html", {"reservation": reservation, "utilisateurs": utilisateurs, "voitures": voitures})

        if dateFin < dateDebut:
            messages.error(request, "La date de fin doit être >= date de début.")
            return render(request, "reservations/modifier.html", {"reservation": reservation, "utilisateurs": utilisateurs, "voitures": voitures})

        # Récupérer les objets
        utilisateur = Utilisateur.objects.get(id=utilisateur_id)
        nouvelle_voiture = Voiture.objects.get(id=voiture_id)

       # Vérifier les chevauchements (exclure la réservation actuelle)
        chevauchement = Reservation.objects.filter(
            voiture=nouvelle_voiture,
            statutR__in=['EN_ATTENTE', 'CONFIRMEE', 'ANNULEE'],
            dateDebut__lte=dateFin,
            dateFin__gte=dateDebut
        ).exclude(id=reservation.id).exists()
        
        if chevauchement:
            messages.error(request, "Cette voiture est déjà réservée pour cette période.")
            return render(request, "reservations/modifier.html", {"reservation": reservation, "utilisateurs": utilisateurs, "voitures": voitures })

        # Recalcul du montant
        nb_jours = (dateFin - dateDebut).days + 1
        montant = nb_jours * nouvelle_voiture.prix_jour
        
        reservation.utilisateur = utilisateur
        reservation.voiture = nouvelle_voiture
        reservation.dateDebut = dateDebut
        reservation.dateFin = dateFin
        reservation.statutR = statutR
        reservation.montant = montant

        reservation.save()
        messages.success(request, "Réservation modifiée avec succès")
        return redirect("liste_reservations")

    return render(request, "reservations/modifier.html", {"reservation": reservation, "utilisateurs": utilisateurs, "voitures": voitures})

# Supprimer une réservation
def supprimer_reservations(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == "POST":
        reservation.delete()
        messages.success(request, "Réservation supprimée avec succès")
        return redirect("liste_reservations")
    return render(request, "reservations/suppression.html", {"reservation": reservation})

# Reserver voiture
def reserver_voiture(request):
    voiture_id = request.GET.get("voiture_id")
    if not voiture_id:
        messages.error(request, "Aucune voiture sélectionnée.")
        return redirect("Veyra")
    
    try:
        voiture = Voiture.objects.get(id=voiture_id, disponibilite=True)
    except Voiture.DoesNotExist:
        messages.error(request, "Véhicule introuvable ou indisponible.")
        return redirect("Veyra")

    # Vérifier si l'utilisateur est connecté
    utilisateur_id = request.session.get("utilisateur_id")
    if not utilisateur_id:
        messages.warning(request, "Vous devez être connecté pour réserver.")
        return redirect("connexion")
    
    if request.method == "POST":
        dateDebut_str = request.POST.get("dateDebut")
        dateFin_str = request.POST.get("dateFin")

        try:
            dateDebut = datetime.strptime(dateDebut_str, "%Y-%m-%d").date()
            dateFin = datetime.strptime(dateFin_str, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            messages.error(request, "Format de date invalide.")
            return render(request, "reservations/reserver_voiture.html", {"voiture": voiture})

        # Validations
        if dateDebut < timezone.now().date():
            messages.error(request, "La date de début doit être aujourd'hui ou plus tard.")
            return render(request, "reservations/reserver_voiture.html", {"voiture": voiture})

        if dateFin <= dateDebut:
            messages.error(request, "La date de fin doit être après la date de début.")
            return render(request, "reservations/reserver_voiture.html", {"voiture": voiture})

        # Vérifier les chevauchements
        chevauchement = Reservation.objects.filter(
            voiture=voiture,
            statutR__in=['EN_ATTENTE', 'CONFIRMEE', 'ANNULEE'],
            dateDebut__lte=dateFin,
            dateFin__gte=dateDebut
        ).exists()
        
        if chevauchement:
            messages.error(request, "Cette voiture est déjà réservée pour cette période. Veuillez choisir d'autres dates.")
            return render(request, "reservations/reserver_voiture.html", {"voiture": voiture})
        
        try:
            utilisateur = Utilisateur.objects.get(id=utilisateur_id)

            # Calcul du montant
            nb_jours = (dateFin - dateDebut).days + 1 
            montant = nb_jours * voiture.prix_jour

            reservation = Reservation.objects.create(
                utilisateur=utilisateur,
                voiture=voiture,
                dateDebut=dateDebut,
                dateFin=dateFin,
                montant=montant,
                statutR="EN_ATTENTE"
            )
            messages.success(request, f"Réservation {reservation.numero} créée avec succès ! Montant total : {montant:,.0f} FCFA")
            return redirect("mes_reservations")
            
        except Utilisateur.DoesNotExist:
            messages.error(request, "Utilisateur introuvable.")
            return redirect("connexion")

    return render(request, "reservations/reserver_voiture.html", {"voiture": voiture})

# Mes reservation
def mes_reservations(request):
    utilisateur_id = request.session.get("utilisateur_id")
    
    if not utilisateur_id:
        messages.error(request, "Vous devez être connecté pour voir vos réservations.")
        return redirect("connexion")
    
    try:
        utilisateur = Utilisateur.objects.get(id=utilisateur_id)
    except Utilisateur.DoesNotExist:
        messages.error(request, "Utilisateur introuvable.")
        return redirect("connexion")
    
    # Récupérer les réservations de cet utilisateur
    reservations = Reservation.objects.filter(utilisateur=utilisateur).select_related('voiture').order_by('-date_creation')
    
    # Statistiques
    total_reservations = reservations.count()
    confirmees_count = reservations.filter(statutR='CONFIRMEE').count()
    en_attente_count = reservations.filter(statutR='EN_ATTENTE').count()
    annulee_count = reservations.filter(statutR='ANNULEE').count()

    # Total dépensé
    from django.db.models import Sum
    total_depense = reservations.filter(
        statutR__in=['CONFIRMEE', 'CONFIRMEE']
    ).aggregate(total=Sum('montant'))['total'] or 0

    # Réservations récentes (les 5 dernières)
    reservations_recentes = reservations[:5]
    
    context = {
        'reservations': reservations,
        'total_reservations': total_reservations,
        'reservations_recentes': reservations_recentes,
        'confirmees_count': confirmees_count,
        'annulee_count': annulee_count,
        'en_attente_count': en_attente_count,
        'total_depense': total_depense,
        'utilisateur': utilisateur,
    }
    
    return render(request, 'reservations/mes_reservations.html', context)

# Historique reservation
def historique_reservations(request):
    reservations_terminees = Reservation.objects.filter(
        utilisateur=request.user,
        statutR__in=['CONFIRMEE', 'ANNULEE'] 
    ).order_by('-dateCreation')
    
    context = {
        'reservations': reservations_terminees,
        'title': 'Historique des Réservations'
    }
    return render(request, 'reservations/historique.html', context)



# ============================================================================================================
# PAIEMENT
# ============================================================================================================
# Liste des paiements
def liste_paiements(request):
    paiements = Paiement.objects.all()
    
    search = request.GET.get("search", "")
    if search:
        paiements = paiements.filter(
            Q(reservation__icontains=search) 
           # Q(voiture__icontains=search) 
           # Q(annee__icontains=search) |
        )
    statutP = request.GET.get('statutP', '')
    if statutP:
        paiements = paiements.filter(statutP=statutP)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(paiements, 5)
    page_obj = paginator.get_page(page_number)
    
    return render(request, "paiements/liste.html", {"paiements": page_obj,"search": search, "statutP": statutP})

# Ajouter un paiement
def ajouter_paiements(request):
    reservations = Reservation.objects.all()

    if request.method == "POST":
        reservation_id = request.POST.get("reservation")
        reservation = get_object_or_404(Reservation, id=reservation_id)
        datePaiement = request.POST.get("datePaiement")
        moyenPaiement = request.POST.get("moyenPaiement")
        statutP = request.POST.get("statutP")

         # Validation: datePaiement > aujourd'hui
        if datePaiement < str(timezone.now().date()):
            messages.error(request, "La date de paiement doit être supérieure ou égale à la date du jour.")
            return render(request, "paiements/ajouter.html", { "reservation": reservations})
        
      
        paiement = Paiement(
            reservation=reservation,
            datePaiement=datePaiement,
            montant=reservation.montant,  # montant repris de la réservation
            moyenPaiement=moyenPaiement,
            statutP=statutP,
        )
        paiement.save()
        messages.success(request, "Paiement enregistré avec succès.")
        return redirect("liste_paiements")

    return render(request, "paiements/ajouter.html", {"reservations": reservations})

# Modifier un paiement
def modifier_paiements(request, id):
    paiement = get_object_or_404(Paiement, id=id)
    reservations = Reservation.objects.all()

    if request.method == "POST":
        reservation_id = request.POST.get("reservation")
        paiement.reservation = Reservation.objects.get(id=reservation_id)
        paiement.datePaiement = request.POST.get("datePaiement")
        paiement.moyenPaiement = request.POST.get("moyenPaiement")
        paiement.statutP = request.POST.get("statutP")

         # Validation: datePaiement > aujourd'hui
        if paiement.datePaiement < str(timezone.now().date()):
            messages.error(request, "La date de paiement doit être supérieure ou égale à la date du jour.")
            return render(request, "paiements/modifier.html", { "reservations": reservations})
        
        paiement.save()
        messages.success(request, "Paiement modifié avec succès.")
        return redirect("liste_paiements")

    return render(request, "paiements/modifier.html", {"paiement": paiement, "reservations": reservations})

# Supprimer un paiements
def supprimer_paiements(request, id):
    paiement = get_object_or_404(Paiement, id=id)
    if request.method == "POST":
        paiement.delete()
        messages.success(request, "Paiement supprimé avec succès")
        return redirect("liste_paiements")
    return render(request, "paiements/suppression.html", {"paiement": paiement})



# ============================================================================================================
# AVIS
# ============================================================================================================
# Liste des avis
def liste_avis(request):
    avis = Avis.objects.all()
    
    search = request.GET.get("search", "")
    if search:
        avis = avis.filter(
            Q(utilisateur__icontains=search) |
            Q(voiture__icontains=search) 
           # Q(annee__icontains=search) |
        )
    statutP = request.GET.get('statutP', '')
    if statutP:
        avis = avis.filter(statutP=statutP)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(avis, 5)
    page_obj = paginator.get_page(page_number)
    
    return render(request, "avis/liste.html", {"avis": page_obj,"search": search, "statutP": statutP})

# Ajouter un avis
def ajouter_avis(request):
    utilisateurs = Utilisateur.objects.filter(role='client')
    voitures = Voiture.objects.all()

    if request.method == "POST":
        utilisateur_id = request.POST.get("utilisateur")
        voiture_id = request.POST.get("voiture")
        note = request.POST.get("note")
        commentaire = request.POST.get("commentaire", "")
        dateAvis = request.POST.get("dateAvis")
        
         # Validation: dateAvis > aujourd'hui
        if dateAvis < str(timezone.now().date()):
            messages.error(request, "La date de l'avis doit être supérieure ou égale à la date du jour.")
            return render(request, "avis/ajouter.html", { "utilisateurs": utilisateurs, "voitures": voitures})
        
        avis = Avis(
            utilisateur=Utilisateur.objects.get(id=utilisateur_id),
            voiture=Voiture.objects.get(id=voiture_id),
            note=note,
            commentaire=commentaire,
            dateAvis=dateAvis
        )
        avis.save()
        messages.success(request, "Avis ajouté avec succès")
        return redirect("liste_avis")

    return render(request, "avis/ajouter.html", {"utilisateurs": utilisateurs, "voitures": voitures})

# Modifier un avis
def modifier_avis(request, id):
    avis = get_object_or_404(Avis, id=id)
    utilisateurs = Utilisateur.objects.filter(role='client')
    voitures = Voiture.objects.all()

    if request.method == "POST":
        utilisateur_id = request.POST.get("utilisateur")
        avis.utilisateur = Utilisateur.objects.get(id=utilisateur_id)
        voiture_id = request.POST.get("voiture")
        avis.voiture = Voiture.objects.get(id=voiture_id)
        avis.note = request.POST.get("note")
        avis.commentaire = request.POST.get("commentaire", "")
        avis.dateAvis = request.POST.get("dateAvis")

         # Validation: dateAvis > aujourd'hui
        if avis.dateAvis < str(timezone.now().date()):
            messages.error(request, "La date de l'avis doit être supérieure ou égale à la date du jour.")
            return render(request, "avis/modifier.html", { "utilisateurs": utilisateurs, "voitures": voitures})
        
        avis.save()
        messages.success(request, "Avis modifié avec succès")
        return redirect("liste_avis")

    return render(request, "avis/modifier.html", {"avis": avis, "utilisateurs": utilisateurs, "voitures": voitures})

# Supprimer un avis
def supprimer_avis(request, id):
    avis = get_object_or_404(Avis, id=id)
    if request.method == "POST":
        avis.delete()
        messages.success(request, "Avis supprimé avec succès")
        return redirect("liste_avis")
    return render(request, "avis/suppression.html", {"avis": avis})