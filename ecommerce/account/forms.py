#DJango
from typing import Any
#mengimpor Any dari modul typing untuk anotasi tipe yang mungkin digunakan nanti
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#mengimpor UserCreationForm dari django.contrib.auth.forms, sebuah form bawaan Django untuk membuat pengguna baru
from django.contrib.auth.models import User
#mengimpor model User dari django.contrib.auth.models, yang merupakan model bawaan Django untuk pengguna
from django import forms
#mengimpor modul forms dari Django, yang menyediakan alat untuk membuat dan menangani formulir HTML
from django.forms.widgets import PasswordInput, TextInput

#Registration Form
class CreateUserForm(UserCreationForm):
#mendefinisikan kelas CreateUserForm yang mewarisi dari UserCreationForm
    class Meta:
    #mendefinisikan kelas Meta untuk menyimpan metadata tentang formulir
        model=User
        #menetapkan model yang digunakan oleh formulir ini adalah model User
        fields=['username', 'email', 'password1', 'password2']
        #menentukan bidang (fields) yang akan ditampilkan di formulir: username, email, password1, dan password2
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
    ##mendefinisikan metode init untuk inisialisasi objek form
    #memanggil metode init dari kelas induk (UserCreationForm) untuk memastikan form diinisialisasi dengan benar
        self.fields['email'].required=True
        #make email as required

#email validation
    def clean_email(self):
    #mendefinisikan metode clean_email untuk validasi email custom
    #bikin variabel email
    #getting attribute email
        email=self.cleaned_data.get("email")
        #mengambil nilai email dari data yang telah dibersihkan (cleaned_data)
        if User.objects.filter(email=email).exists():
        #memeriksa apakah ada pengguna dengan email yang sama di database
            raise forms.validationError('This email is invalid')
            #jika email sudah ada, mengangkat pengecualian ValidationError dengan pesan bahwa email tidak valid
        if len(email)>=350:
        #memeriksa apakah panjang email lebih dari atau sama dengan 350 karakter
            raise forms.ValidationError("Your email is too long")
            #jiika email terlalu panjang, mengangkat pengecualian ValidationError dengan pesan bahwa email terlalu panjang
        return email


#Log In Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

#Update Form
class UpdateUserForm(forms.ModelForm):
    password = None
    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        #mendefinisikan metode init untuk inisialisasi objek form
        #memanggil metode init dari kelas induk (UserCreationForm) untuk memastikan form diinisialisasi dengan benar
        self.fields['email'].required=True
        #make email as required
    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']

