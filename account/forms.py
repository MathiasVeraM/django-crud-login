from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Usuario
from django.utils.translation import gettext_lazy as _
import datetime

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label=_("Correo Electrónico"))
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ("username", "email", "date_of_birth")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs.update({
            "class": "input",
            "placeholder": "Nombre de usuario (ej: pepito123)"
        })
        
        self.fields["email"].widget.attrs.update({
            "class": "input",
            "placeholder": "Correo electrónico válido (ej: pepe@gmail.com)"
        })
        
        self.fields["date_of_birth"].widget.attrs.update({
            "class": "input",
            "placeholder": "AAAA-MM-DD (ej: 2000-01-01)",
            "type": "date"
        })
        
        self.fields["password1"].widget.attrs.update({
            "class": "input",
            "placeholder": "Contraseña (ej: Pepito123@)"
        })
        
        self.fields["password2"].widget.attrs.update({
            "class": "input",
            "placeholder": "Repite la contraseña (ej: Pepito123@)"
        })
        
    def clean_date_of_birth(self):
        dob = self.cleaned_data.get("date_of_birth")
        if dob:
            today = datetime.date.today()
            if dob > today:
                raise forms.ValidationError("La fecha de nacimiento no puede ser en el futuro.")
        return dob
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        # TODO : VALIDAR QUE SEA UNIQUE A FUTURO
        return email
    
class CustomUserChangeForm(UserChangeForm):
    password = None # No se puede cambiar la contraseña
    
    class Meta:
        model = Usuario
        fields = ("username", "email", "date_of_birth", "first_name", "last_name")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for fname in ("username", "email", "first_name", "last_name", "date_of_birth"):
            if fname in self.fields:
                self.fields[fname].widget.attrs.update({
                    "class": "input",
                })
        if "date_of_birth" in self.fields:
            self.fields["date_of_birth"].widget.attrs.update({"type": "date"})
            
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        "class": "input",
        "placeholder": "Nombre de usuario (ej: pepito123)"
    }))
    
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={
        "class": "input",
        "placeholder": "Contraseña (ej: Pepito123@)"
    }))