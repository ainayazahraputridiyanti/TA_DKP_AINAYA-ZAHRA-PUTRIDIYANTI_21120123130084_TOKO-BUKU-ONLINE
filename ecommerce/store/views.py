#store: menampilkan semua produk
#categories: mengembalikan semua kategori
#list_category: menampilkan produk berdasarkan kategori yang dipilih
#product_info: menampilkan detail produk berdasarkan slug produk yang dipilih

from django.shortcuts import render
#mengimpor fungsi render untuk merender template dengan konteks tertentu
from . models import Category, Product
#mengimpor model Category dan Product dari modul lokal models
from django.shortcuts import get_object_or_404
#mengimpor fungsi get_object_or_404 untuk mendapatkan objek dari database atau mengembalikan error 404 jika objek tidak ditemukan

# Create your views here.

#buat fungsi store untuk menampilkan semua produk
def store(request): #to handle the view
    all_products = Product.objects.all()
    context = {'my_products': all_products}
    return render(request, 'store/store.html', context) #lokasinya
#mengambil semua produk dari database
#menyimpan produk dalam konteks
#merender template store/store.html dengan konteks tersebut

#buat fungsi categories untuk mengembalikan semua kategori
def categories(request): 
    #mendefinisikan sebuah fungsi bernama categories yang menerima satu argumen request
    #argumen request biasanya berisi informasi tentang permintaan HTTP yang diterima oleh server
    all_categories = Category.objects.all()
    #query yang meminta semua objek atau entri dari tabel Category
    #hasilnya adalah semua kategori yang ada dalam database, disimpan dalam variabel all_categories
    return {'all_categories': all_categories}
    #mengembalikan all_categories nilainya adalah objek all_categories yang berisi semua kategori yang diambil dari database
#mengambil semua kategori dari database
#mengembalikan semua kategori sebagai konteks

#buat fungsi list_category untuk menampilkan produk berdasarkan kategori yang dipilih
def list_category(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    #filter kategorinya
    return render(request, 'store/list-category.html', {'category':category, 'products':products})
#mendapatkan kategori berdasarkan slug, atau mengembalikan error 404 jika tidak ditemukan
#menyaring produk berdasarkan kategori tersebut
#merender template store/list-category.html dengan konteks kategori dan produk yang difilter

#buat fungsi product_info untuk menampilkan detail produk berdasarkan slug produk yang dipilih
def product_info(request, product_slug):
    #get data from our database
    product = get_object_or_404(Product, slug=product_slug)
    #get our products from a database, kalo ga ada error
    #slug nya sama kayak yang di database product
    context = {'product': product}
    return render(request, 'store/product-info.html', context)
#mendapatkan produk berdasarkan slug, atau mengembalikan error 404 jika tidak ditemukan
#menyimpan produk dalam konteks
#merender template store/product-info.html dengan konteks tersebut

#**render = mengambil data dan template, menggabungkannya, dan menghasilkan HTML yang siap dikirim ke browser
#di Django, fungsi render digunakan untuk memproses template dengan konteks data dan menghasilkan respons HTTP