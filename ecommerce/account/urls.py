#menghubungkan pola URL dengan fungsi view dalam aplikasi Django menggunakan modul django.urls

from django.urls import path
#mengimpor fungsi path dari modul django.urls untuk menentukan pola URL dan menautkannya dengan view

from . import views
#mengimpor file views.py dari direktori yang sama
#views adalah file yang berisi definisi tampilan
#. karena in the same directory

urlpatterns = [
#daftar yang berisi definisi pola URL dan view yang akan ditautkan
#Setiap pola URL didefinisikan dengan format path('polanya/', views.namaview, name='nama-url')

    path('register', views.register, name='register'),
    #menentukan pola URL kosong ('') yang akan ditautkan ke view register yang terdapat di modul views.py
    #memberikan nama URL yaitu 'register'

]    