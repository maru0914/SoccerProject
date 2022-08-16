from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
   
    class Meta:
        model = User
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
