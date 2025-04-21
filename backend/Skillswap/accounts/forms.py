from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model

# Убедитесь, что вы импортируете модель Skill из правильного места (вашего приложения Application)
from Application.models import Skill


User = get_user_model()

class CustomUserCreationForm(BaseUserCreationForm):
    # Поля first_name, last_name, email могут быть необязательными при создании пользователя в базовом классе,
    # но здесь они явно определены. Используйте required=True если они обязательны.
    first_name = forms.CharField(max_length=150, required=False, label='Имя')
    last_name = forms.CharField(max_length=150, required=False, label='Фамилия')
    email = forms.EmailField(required=True, label='Email')

    # ИЗМЕНЕНО: Используйте ModelChoiceField для ForeignKey
    skill = forms.ModelChoiceField(
        queryset=Skill.objects.all(),
        required=False, # Соответствует null=True в модели
        label='Основной навык' # Изменена метка для ясности
    )

    class Meta(BaseUserCreationForm.Meta):
        model = User
      
        fields = ('username', 'email', 'first_name', 'last_name', 'skill')


    def save(self, commit=True):
   
        user = super().save(commit=False)

        # Присваиваем данные из очищенных данных формы
        user.first_name = self.cleaned_data.get("first_name", "") # Используем .get() для необязательных полей
        user.last_name = self.cleaned_data.get("last_name", "")   # Используем .get()
        user.email = self.cleaned_data["email"] # Email обычно обязателен
        user.skill = self.cleaned_data.get("skill", None) # <-- ЭТА СТРОКА ПРАВИЛЬНО ПРИСВАИВАЕТ НАВЫК

        if commit:
            user.save()

        return user


class ProfileEditForm(forms.ModelForm):
    # ИЗМЕНЕНО: Используйте ModelChoiceField для ForeignKey
    skill = forms.ModelChoiceField( # <-- ИЗМЕНЕНО
        queryset=Skill.objects.all(),
        # Виджет можно оставить Select или изменить на RadioSelect, но не CheckboxSelectMultiple для ModelChoiceField
        # widget=forms.Select, # Пример
        required=False, # Соответствует null=True в модели
        label='Основной навык' # Изменена метка
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'bio', 'skill', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            # Если profile_picture это URLField и вы хотите текстовое поле:
            # 'profile_picture': forms.URLInput(),
        }
        # Если у вас была проблема с email being read-only в ModelForm,
        # уберите его из fields или переопределите поле явно.