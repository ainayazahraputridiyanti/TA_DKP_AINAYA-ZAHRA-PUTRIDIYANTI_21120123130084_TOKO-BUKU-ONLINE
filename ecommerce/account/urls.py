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
    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),
    path('email-verification-sent', views.email_verification_sent, name='email-verification-sent'),
    path('email-verification-success', views.email_verification_success, name='email-verification-success'),
    path('email-verification-failed', views.email_verification_failed, name='email-verification-faiiled'),

    #Log In / Log Out urls
    path('my-login', views.my_login, name='my-login'),
    path('user-logout', views.user_logout, name='user-logout'),
    
    #Dashboard /Profile urls
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile-management', views.profile_management, name='profile-management'),
    path('delete-account', views.delete_account, name='delete-account'),
]    