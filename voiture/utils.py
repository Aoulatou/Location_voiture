from .models import Utilisateur

#Récupère l'utilisateur connecté depuis la session
def get_current_user(request):
    utilisateur_id = request.session.get('utilisateur_id')
    if utilisateur_id:
        try:
            return Utilisateur.objects.get(id=utilisateur_id)
        except Utilisateur.DoesNotExist:
            return None
    return None

#Vérifie si un utilisateur est connecté
def is_user_authenticated(request):
    return request.session.get('utilisateur_id') is not None

#Connecte un utilisateur et creer la session
def login_user(request, user):
    request.session['utilisateur_id'] = user.id
    request.session['utilisateur_nom'] = user.nom
    request.session['utilisateur_prenom'] = user.prenom
    request.session['utilisateur_email'] = user.email
    request.session['utilisateur_role'] = user.role
    request.session.modified = True

#Déconnecte un utilisateur
def logout_user(request):
    request.session.flush()

