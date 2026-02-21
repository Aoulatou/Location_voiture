from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [ 

    path("Veyra", views.accueil, name="Veyra"),
   
    path("connexion/", views.connexion, name="connexion"),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('resend-otp/', views.resend_otp, name='resend_otp'),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
    
    path("inscription/", views.inscription, name="inscription"),
    path('profil/', views.profil, name='profil'), 
    
    path("dashboard/", views.dashboard, name="dashboard"),
#---------------UTILISATEURS--------------------------------------------------------------------------------
    path('utilisateurs/', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('utilisateurs/ajouter/', views.ajouter_utilisateurs, name='ajouter_utilisateurs'),
    path('utilisateurs/modifier/<int:id>/', views.modifier_utilisateurs, name='modifier_utilisateurs'),
    path('utilisateurs/supprimer/<int:id>/', views.supprimer_utilisateurs, name='supprimer_utilisateurs'),
#-----------------------------------------------------------------------------------------------------------

#---------------VOITURES------------------------------------------------------------------------------------
    path('voitures/', views.liste_voitures, name='liste_voitures'),
    path('voitures/ajouter/', views.ajouter_voitures, name='ajouter_voitures'),
    path('voitures/modifier/<int:id>/', views.modifier_voitures, name='modifier_voitures'),
    path('voitures/supprimer/<int:id>/', views.supprimer_voitures, name='supprimer_voitures'),
#----------------------------------------------------------------------------------------------------------- 

#---------------RESERVATIONS------------------------------------------------------------------------------------
    path('reservations/', views.liste_reservations, name='liste_reservations'),
    path('reservations/ajouter/', views.ajouter_reservations, name='ajouter_reservations'),
    path('reservations/modifier/<int:id>/', views.modifier_reservations, name='modifier_reservations'),
    path('reservations/supprimer/<int:id>/', views.supprimer_reservations, name='supprimer_reservations'),
    path('reservations/reserver_voiture/', views.reserver_voiture, name='reserver_voiture'),
    path('reservations/mes_reservations/', views.mes_reservations, name='mes_reservations'),
#----------------------------------------------------------------------------------------------------------- 

#---------------PAIEMENTS------------------------------------------------------------------------------------
    path('paiements/', views.liste_paiements, name='liste_paiements'),
    path('paiements/ajouter/', views.ajouter_paiements, name='ajouter_paiements'),
    path('paiements/modifier/<int:id>/', views.modifier_paiements, name='modifier_paiements'),
    path('paiements/supprimer/<int:id>/', views.supprimer_paiements, name='supprimer_paiements'),
#----------------------------------------------------------------------------------------------------------- 

#---------------AVIS------------------------------------------------------------------------------------
    path('avis/', views.liste_avis, name='liste_avis'),
    path('avis/ajouter/', views.ajouter_avis, name='ajouter_avis'),
    path('avis/modifier/<int:id>/', views.modifier_avis, name='modifier_avis'),
    path('avis/supprimer/<int:id>/', views.supprimer_avis, name='supprimer_avis'),
#----------------------------------------------------------------------------------------------------------- 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

