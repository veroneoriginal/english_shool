from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from user_app.models import User, Role


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')


class TeachersForm(forms.ModelForm):
    username = forms.CharField(label='Имя',
                               required=True,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Input user name',
                                          'class': 'form-control', }
                               )
                               )

    phone_number = forms.CharField(
        label='Номер телефона',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Input your phone number',
                   'class': 'form-control'}
        )
    )

    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Input your email',
                   'class': 'form-control'}
        )
    )

    role = forms.ModelChoiceField(
        queryset=Role.objects.filter(name=Role.TEACHER),
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control',
                   # делает поле недоступным для редактирования пользователем
                   'disabled': 'disabled'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email',)

    # Этот метод является конструктором класса формы и вызывается при создании экземпляра формы
    def __init__(self, *args, **kwargs):
        """Переопределяю метод для того, чтобы избежать доступа к бд в момент определения класса формы"""
        super().__init__(*args, **kwargs)
        # получает объект поля формы 'role'
        self.fields['role'].initial = Role.objects.get(name=Role.TEACHER)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            self.add_error('email', 'Введите корректный email адрес.')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            self.add_error('phone_number', 'Введите корректный номер телефона.')
        return phone_number

    def save(self, commit=True):
        # Вызов родительского метода save с параметром commit=False создает объект User, но не сохраняет его в базе данных.
        # Это позволяет нам выполнить дополнительные действия с объектом перед его сохранением.
        user = super().save()
        teacher_role = Role.objects.get(name=Role.TEACHER)
        user.role.add(teacher_role)
        return user
