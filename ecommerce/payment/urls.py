#menghubungkan pola URL dengan fungsi view dalam aplikasi Django menggunakan modul django.urls

from django.urls import path
#mengimpor fungsi path dari modul django.urls untuk menentukan pola URL dan menautkannya dengan view

from . import views
#mengimpor file views.py dari direktori yang sama
#views adalah file yang berisi definisi tampilan
#. karena in the same directory

urlpatterns = [
    path('payment-success', views.payment_success, name='payment-success'),
    path('payment-failed', views.payment_failed, name='payment-failed'),
]