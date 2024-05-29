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
    path('', views.store, name='store'),
    #menentukan pola URL kosong ('') yang akan ditautkan dengan fungsi store dalam file views.py
    #store (main page)
    path('product/<slug:product_slug>/', views.product_info, name='product-info'), 
    #mengaitkan URL dengan format `/product/nama-produk/` ke view `product_info` dalam aplikasi Django
    #dengan memberikan nama `product-info` pada URLnya
    #bikin slug individual product
    path('search/<slug:category_slug>/', views.list_category, name='list-category')
    #menetapkan URL dengan format `/search/nama-kategori/` ke view `list_category` dalam aplikasi Django,
    #dengan memberikan nama `list-category` pada URLnya
    #bikin slug individual category
]

#penting karena untuk memastikan bahwa aplikasi dapat merespons permintaan dari pengguna dengan benar