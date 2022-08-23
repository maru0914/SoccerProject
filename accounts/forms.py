"""forms setting for accounts app"""
from django.contrib.auth.forms import UserCreationForm

from accounts.models import MyUser


class RegisterUserForm(UserCreationForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""

    class Meta:
        model = MyUser
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['username'].widget.attrs['class'] = 'form-control py-2 mb-2'
        self.fields['username'].widget.attrs['placeholder'] = 'ユーザー名'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control py-2 mb-2'
        self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control py-2 mb-2'
        self.fields['password2'].widget.attrs['placeholder'] = 'パスワード(確認用)'
        self.fields['password2'].label = ''
