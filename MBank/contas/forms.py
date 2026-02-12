from django import forms
from django.contrib.auth.models import User
from .models import Conta


class CadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='senha')
    cpf = forms.CharField(max_length=11, label='CPF( Somente numeros )')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Conta.objects.create(
                usuario=user,
                numero=str(User.objects.count() + 1000)
            )
        return user
