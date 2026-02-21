from django import forms
from .models import Utilisateur
from django.contrib.auth.hashers import make_password

class InscriptionForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label="Confirmer le mot de passe")
    password = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe")

    class Meta:
        model = Utilisateur
        fields = ["nom", "prenom", "email", "telephone", "adresse", "password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")

        # Hash le mot de passe pour le stocker en sécurité
        cleaned_data["password"] = make_password(password)
        return cleaned_data
