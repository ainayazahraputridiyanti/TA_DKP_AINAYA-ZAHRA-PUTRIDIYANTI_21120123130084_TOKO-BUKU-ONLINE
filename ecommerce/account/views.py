from django.shortcuts import redirect, render
#mengimpor fungsi redirect dan render dari django.shortcuts untuk mengarahkan pengguna dan merender template dengan data
from .forms import CreateUserForm, LoginForm, UpdateUserForm
#mengimpor CreateUserForm dari modul forms yang digunakan untuk menangani formulir pendaftaran pengguna
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django.contrib.auth.models import User
#mengimpor model User dari django.contrib.auth.models, yang merupakan model bawaan Django untuk pengguna
from django.contrib.sites.shortcuts import get_current_site

from . token import user_tokenizer_generate

from django.template.loader import render_to_string

from django.utils.encoding import force_bytes, force_str

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

#mendefinisikan fungsi register untuk menangani pendaftaran pengguna baru menggunakan form
def register(request): #definisi view Django yang menangani pendaftaran pengguna baru menggunakan form
#register = menangani permintaan (request) pendaftaran pengguna
    form = CreateUserForm
    #mendefinisikan form yang akan digunakan untuk pendaftaran
    #mengacu ke forms.py
    #if the request.method equal to post
    #if so, then ok
    if request.method == 'POST':
    #mengecek apakah request method adalah POST
    #request POST = pengguna telah mengirimkan form
        form = CreateUserForm(request.POST)
        #membuat instance baru dari CreateUserForm dengan data yang dikirim melalui request POST
        #instance = objek yang dibuat berdasarkan sebuah kelas
        #request.POST retrieve all data that has been submitted to CreateUserForm
        #menangani validasi dan penyimpanan data dari sebuah form
        if form.is_valid():
        #memeriksa data yang dimasukkan ke form itu valid/tidak, kalo iya = true
            user = form.save()
            user.is_active = False
            user.save()
            #email verification setup template
            current_site = get_current_site(request)
            subject = 'Account verification email'
            message = render_to_string('account/registration/email-verification.html', {
                'user' : user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': user_tokenizer_generate.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return redirect('email-verification-sent')



    context = {'form':form} #membuat dictionary context yang berisi form
    #Context adalah sebuah "kantong" yang berisi data yang ingin kita kirimkan ke template (halaman HTML)
    #Context ini akan diteruskan ke template untuk dirender
    return render(request, 'account/registration/register.html', context=context) #merender template register.html yang berada di dalam direktori account/registration, dan meneruskan context ke template tersebut
    #Render adalah proses untuk mengambil template HTML dan mengisi tempat-tempat tertentu dengan data dari context
    #agar pengguna dapat melihat form di halaman web mereka

#email verification URLs
def email_verification(request, uidb64, token):
    unique_id = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=unique_id)
    #success
    if user and user_tokenizer_generate.check_token(user, token):
        user.is_active=True
        user.save()
        return redirect('email-verification-success')
    #failed
    else:
        return redirect('email-verification-failed')
    
def email_verification_sent(request):
    return render(request, 'account/registration/email-verification-sent.html')

def email_verification_success(request):
    return render(request, 'account/registration/email-verification-success.html')

def email_verification_failed(request):
    return render(request, 'account/registration/email-verification-failed.html')

#Log In
def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            
    context = {'form':form}
    return render(request, 'account/my-login.html', context=context)

#Log Out
def user_logout(request):
    auth.logout(request)
    return redirect("store")

@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'account/dashboard.html')

@login_required(login_url='my-login')
def profile_management(request):
    #Updating Username & Email
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')
    user_form = UpdateUserForm(instance=request.user)
    context = {'user_form':user_form}
    return render(request, 'account/profile-management.html', context=context)

@login_required(login_url='my-login')
def delete_account(request):
    #Deleting Account
    user = User.objects.get(id=request.user.id)
    if request.method =='POST':
        user.delete()
        return redirect('store')
    return render(request, 'account/delete-account.html')

#Shipping View
def manage_shipping(request):
    try:
        #Account user with shipment information
        shipping = ShippingAddress.objects.get(user=request.user.id)
    except ShippingAddress.DoesNotExist:
        #Account user with no shipment information
        shipping=None
    form = ShippingForm(instance=shipping)
    if request.method == 'POST':
        form = ShippingForm(request.POST, instance=shipping)
        if form.is_valid():
            #Assign the user FK on the object
            shipping_user = form.save(commit=False)
            shipping_user.user = request.user
            shipping_user.save()
            return redirect('dashboard')
        context = {'form':form}
        return render(request, 'account/manage-shipping.html')

            
