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

    path('', views.cart_summary, name='cart-summary'),
    #menentukan pola URL kosong ('') yang akan ditautkan ke view cart_summary yang terdapat di modul views.py
    #memberikan nama URL yaitu 'cart-summary'

    path('add/', views.cart_add, name='cart-add'),
    #menetapkan tautan untuk URL 'add/' ke view cart_add dalam modul views.py
    #memberikan nama URL yaitu 'cart-add'

    path('delete/', views.cart_delete, name='cart-delete'),
    #menetapkan tautan untuk URL 'delete/' ke view cart_delete dalam modul views.py
    #memberikan nama URL yaitu 'cart-delete'

    path('update/', views.cart_update, name='cart-update'),
    #menetapkan tautan untuk URL 'update/' ke view cart_update dalam modul views.py
    #memberikan nama URL yaitu 'cart-update'
]

#penting karena untuk memastikan bahwa aplikasi dapat merespons permintaan dari pengguna dengan benar