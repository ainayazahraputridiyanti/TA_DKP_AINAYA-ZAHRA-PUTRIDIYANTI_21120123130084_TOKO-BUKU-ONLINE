from django.shortcuts import redirect, render
#mengimpor fungsi redirect dan render dari django.shortcuts untuk mengarahkan pengguna dan merender template dengan data
from .forms import CreateUserForm
#mengimpor CreateUserForm dari modul forms yang digunakan untuk menangani formulir pendaftaran pengguna

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
            form.save()
            #menyimpan data yang valid ke dalam database
            return redirect('')
            #setelah data berhasil disimpan, user akan diarahkan ke URL lain
    context = {'form':form} #membuat dictionary context yang berisi form
    #Context adalah sebuah "kantong" yang berisi data yang ingin kita kirimkan ke template (halaman HTML)
    #Context ini akan diteruskan ke template untuk dirender
    return render(request, 'account/registration/register.html', context=context) #merender template register.html yang berada di dalam direktori account/registration, dan meneruskan context ke template tersebut
    #Render adalah proses untuk mengambil template HTML dan mengisi tempat-tempat tertentu dengan data dari context
    #agar pengguna dapat melihat form di halaman web mereka
