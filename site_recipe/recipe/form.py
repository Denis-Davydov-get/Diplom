from django import forms


class ImageForm(forms.Form):
    image = forms.ImageField()


# форма создания новго товара
class UserRegistrationForm(forms.Form):
    name = forms.CharField(label="Имя")
    email = forms.EmailField(label='Your email address', max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class UserLoginForm(forms.Form):
    name = forms.CharField(label="Имя")
    password = forms.CharField(widget=forms.PasswordInput)
