from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from api.models import Skill


User = get_user_model()

from api.models import Skill  # Убедись, что путь правильный

class CustomUserCreationForm(BaseUserCreationForm):
    first_name = forms.CharField(max_length=150, required=False, label='Name')
    last_name = forms.CharField(max_length=150, required=False, label='SureName')
    email = forms.EmailField(required=True, label='Email')
    
    skill = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.SelectMultiple,
        required=False,
        label='Навыки'
    )

    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'skill', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Ensure 'skill' is set as a related manager, using 'set()' for a many-to-many relationship
            if self.cleaned_data['skill']:
                user.skill.set(self.cleaned_data['skill'])  # Correctly associate the skills
        return user

    

from django import forms
from .models import User, Skill  # Убедись, что Skill импортирован

class ProfileEditForm(forms.ModelForm):
    skill = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Skills'  
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'bio', 'skill', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }
