#membuat sebuah variabel yang dapat diakses di setiap template Django, yang berisi instance dari kelas Cart
#instance kelas Cart ini dapat digunakan di dalam template untuk menampilkan informasi keranjang belanja (jumlah item atau total harga)
    #instance=salinan sebuah kelas yang telah dibuat dan diinisialisasi, punya atribut dan perilaku yang ditentukan oleh kelas itu

#mengimpor kelas Cart dari modul cart di dalam folder yang sama dengan file di sini (ditandai .)
from .cart import Cart

#mendefinisikan fungsi cart dan mengambil satu parameter request
def cart(request):
    #membuat dictionary yang berisi sebuah variabel 'cart'
    #yang memuat instance dari kelas Cart yang dibuat menggunakan request sebagai argumen
    return {'cart': Cart(request)}
    #cart = variabel dalam setiap template Django
    #nilainya adalah instance dari kelas Cart yang dibuat dengan menggunakan request sebagai argumen