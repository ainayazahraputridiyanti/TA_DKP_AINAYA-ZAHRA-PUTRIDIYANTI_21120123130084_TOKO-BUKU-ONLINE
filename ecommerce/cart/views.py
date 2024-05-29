from django.shortcuts import render
#import fungsi render dari modul django.shortcuts
from .cart import Cart
#import kelas Cart dari modul .cart dalam paket yang sama
from store.models import Product
#import model Product dari aplikasi store
from django.shortcuts import get_object_or_404
#import fungsi get_object_or_404 dari Django untuk mendapatkan objek atau menampilkan halaman 404 jika tidak ditemukan
from django.http import JsonResponse
#import kelas JsonResponse dari Django untuk mengembalikan respons dalam format JSON

# Create your views here.

#menampilkan ringkasan keranjang belanja ke pengguna
def cart_summary(request):
#mendefinisikan fungsi cart_summary yang menerima permintaan (request) dari pengguna
    cart = Cart(request)
    #fungsi membuat objek keranjang belanja yang bergantung pada informasi dari permintaan pengguna
    return render(request, 'cart/cart-summary.html', {'cart':cart})
    #mengembalikan respons dengan menggunakan template cart-summary.html dan menyertakan objek cart sebagai konteks

#menambahkan produk ke keranjang belanja
def cart_add(request):
    cart = Cart(request)
    #menambahkan produk dari keranjang belanja berdasarkan permintaan pengguna
    #objek keranjang belanja dibuat dengan menggunakan informasi dari permintaan pengguna

    #ajax = checking the action
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
    #fungsi cart_add menginisialisasi objek keranjang belanja dengan menggunakan informasi dari permintaan pengguna
    #lalu memeriksa apakah permintaan dikirim melalui metode POST
    #jika action yang dikirim adalah post, maka fungsi akan mengambil ID produk dari permintaan
        if product_id:
            try: 
                product_id = int(product_id) 
            except ValueError: 
                pass
        #memeriksa apakah product_id tidak kosong
        #jika product_id ada akan dikonversi jadi integer
        #jika konversi gagal, ValueError akan melakukan pass
        #pass = tidak mengambil tindakan dan kode berikutnya tidak dieksekusi
            else:
                product_quantity = int(request.POST.get('product_quantity'))
                product = get_object_or_404(Product, id=product_id)
                cart.add(product=product, product_qty=product_quantity)
                cart_quantity = cart.__len__()
                response = JsonResponse({'qty': product_quantity})
                return response
            #jika konversi berhasil,
            #akan mengambil nilai 'product_quantity' dari data POST dan mengonversinya jadi integer
            #di sini tidak ada penanganan kesalahan, jadi akan diasumsi kalo data yang dikirim selalu valid
            #ambil product_quantity: ambil dan konversi nilai product_quantity dari data POST menjadi integer
            #dapatkan produk: cari objek produk dengan product_id, jika tidak ditemukan kembalikan 404
            #tambahkan ke keranjang: tambahkan produk tersebut ke dalam keranjang dengan jumlah yang ditentukan
            #hitung total item: hitung jumlah total item dalam keranjang (tidak digunakan lebih lanjut)
            #kirim respons JSON: buat dan kirim respons JSON yang berisi jumlah produk yang ditambahkan
        else:
            pass
        #jika kondisi sebelumnya tidak terpenuhi, tidak ada tindakan yang diambil
        #eksekusi program akan melanjutkan ke baris kode berikutnya di luar blok kondisi

#menghapus produk dari keranjang belanja
def cart_delete(request):
    cart = Cart(request)
    #menghapus produk dari keranjang belanja berdasarkan permintaan pengguna
    #objek keranjang belanja dibuat dengan menggunakan informasi dari permintaan pengguna
    
    #ajax = checking the action
    if request.POST.get('action') == 'post': 
    #fungsi cart_delete menginisialisasi objek keranjang belanja dengan menggunakan informasi dari permintaan pengguna
    #lalu memeriksa apakah permintaan dikirim melalui metode POST
    #jika action yang dikirim adalah post, maka fungsi akan mengambil ID produk dari permintaan
        product_id = int(request.POST.get('product_id'))
        #mengambil ID produk yang dikirim dalam permintaan dan mengonversinya menjadi bilangan bulat
        cart.delete(product=product_id)
        #menghapus produk yang memiliki ID yang sesuai dari keranjang belanja
        cart_quantity = cart.__len__()
        #mengambil jumlah item dalam keranjang belanja
        cart_total = cart.get_total()
        #mengambil total harga dari keranjang belanja
        response = JsonResponse({'qty': cart_quantity, 'total': cart_total})
        #membuat respons dalam format JSON yang berisi jumlah item dan total harga baru dalam keranjang belanja
        return response
        #mengembalikan respons JSON kepada pengguna

#memperbarui jumlah produk dalam keranjang belanja
def cart_update(request):
    cart = Cart(request)
    #memperbarui produk dari keranjang belanja berdasarkan permintaan pengguna
    #objek keranjang belanja dibuat dengan menggunakan informasi dari permintaan pengguna

    #ajax = checking the action
    if request.POST.get('action') == 'post':
    #fungsi cart_update menginisialisasi objek keranjang belanja dengan menggunakan informasi dari permintaan pengguna
    #lalu memeriksa apakah permintaan dikirim melalui metode POST
    #jika action yang dikirim adalah post, maka fungsi akan mengambil ID produk dari permintaan
        product_id = int(request.POST.get('product_id'))
        #mengambil ID produk yang dikirim dalam permintaan dan mengonversinya menjadi bilangan bulat
        product_quantity = int(request.POST.get('product_quantity'))
        #mengambil jumlah produk yang baru dalam permintaan dan mengonversinya menjadi bilangan bulat
        cart.update(product=product_id, qty=product_quantity)
        #memperbarui jumlah produk dalam keranjang belanja dengan menggunakan ID produk dan jumlah produk yang baru
        cart_quantity = cart.__len__()
        #mengambil jumlah total item dalam keranjang belanja
        cart_total = cart.get_total()
        #engambil total harga dari keranjang belanja
        response = JsonResponse({'qty': cart_quantity, 'total': cart_total})
        #membuat respons dalam format JSON yang berisi jumlah item dan total harga baru dalam keranjang belanja
        return response
        #mengembalikan respons JSON kepada pengguna