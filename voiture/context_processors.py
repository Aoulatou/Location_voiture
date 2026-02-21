from .utils import get_current_user, is_user_authenticated

def auth_context(request):
    """Ajoute l'utilisateur au contexte de tous les templates"""
    current_user = get_current_user(request)
    
    # Créer un objet user similaire à Django User avec is_authenticated
    class CustomUserProxy:
        def __init__(self, user):
            if user:
                self.id = user.id
                self.nom = user.nom
                self.prenom = user.prenom
                self.email = user.email
                self.telephone = user.telephone
                self.adresse = user.adresse
                self.role = user.role
                self.is_authenticated = True
                self.first_name = user.prenom
                self.username = user.email
            else:
                self.is_authenticated = False
                self.id = None
                self.nom = None
                self.prenom = None
                self.email = None
                self.first_name = None
                self.username = None
    
    return {
        'user': CustomUserProxy(current_user),
    }