from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from .utils import is_user_authenticated
from .utils import get_current_user

def login_required(view_func):
    #Décorateur pour exiger une connexion
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if not is_user_authenticated(request):
            messages.warning(request, 'Vous devez être connecté pour accéder à cette page')
            return redirect('connexion')
        return view_func(request, *args, **kwargs)
    return wrapped_view

def role_required(allowed_roles):
    #Décorateur pour exiger un rôle spécifique
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if not is_user_authenticated(request):
                messages.warning(request, 'Vous devez être connecté pour accéder à cette page')
                return redirect('connexion')
            
            user = get_current_user(request)
            if user.role not in allowed_roles:
                messages.error(request, 'Vous n\'avez pas les permissions nécessaires')
                return redirect('Veyra')
            
            return view_func(request, *args, **kwargs)
        return wrapped_view
    return decorator