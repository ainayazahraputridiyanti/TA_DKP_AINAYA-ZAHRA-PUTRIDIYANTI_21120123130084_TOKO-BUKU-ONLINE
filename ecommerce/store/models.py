#mendefinisikan model untuk Category dan Product dalam aplikasi Django
#dengan atribut-atribut yang menyimpan informasi seperti nama, deskripsi, dan harga, serta fungsi untuk menghasilkan URL absolut untuk setiap objek

from django.db import models
# mengimpor modul models yang digunakan untuk mendefinisikan struktur database dalam aplikasi Django
from django.urls import reverse
#allows to create own url
#mengimpor fungsi reverse yang memungkinkan pembuatan URL berdasarkan nama yang terdaftar dalam pengaturan URL aplikasi

# Create your models here.
class Category(models.Model):
    #Kategori itu dibuat jenis barang misal buku, baju, dll
    name = models.CharField(max_length=250, db_index=True)
    #name itu buat nama kategorinya
    #max length itu limit karakternya
    #db index is to improve memory usage and for faster lookups in our database table
    #db index itu akan berhenti nyari kalo data yang dicari sudah ketemu, jadi ga perlu nyari keseluruhan data modelnya
    slug = models.SlugField(max_length=250, unique=True)
    #slug kayak misal https://... nah slug itu akan muncul setelah "/"
    #max length itu limit karakternya
    #unique kategori itu biar masing2 itu 1, jadi kategori "sepatu" itu cuma ada 1
    class Meta:
        verbose_name_plural = 'categories'
        #gunanya biar pluralnya jadi "categories instead of categorys"

    def __str__(self): #string function
        return self.name
    #return ini biar namanya muncul, jadi bukan "category 1" tapi yang muncul nanti namanya

    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])
    #custom url
    #args=[self.slug] adalah daftar argumen yang akan dimasukkan ke dalam pola URL, self.slug adalah nilai slug dari objek saat ini


class Product(models.Model):
#Bikin produk
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    #nyambungin kategori dan produk
    #Category to linked categoryand  modul
    #related_name to help establish relationships between our category model and our product model
    #kalo kategorinya dihapus, nanti otomatis kehapus 
    #null = true is to make sure we don't have any null objects
    title = models.CharField(max_length=250)
    #title itu untuk kayak nama produknya, misal Ralph Lauren Shirt
    brand = models.CharField(max_length=250, default='un-branded')
    #max length itu limit karakternya
    #unbranded for items that are not clearly identified with a brand or mark identifying the brand
    description = models.TextField(blank=True)
    #textfield is for a lot of characters, lebih panjang daripada charfield
    #blank = true itu agar opsional, jadi kalo kosong alias ga ada isinya itu gapapa
    slug = models.SlugField(max_length=255)
    #slug kayak misal https://... nah slug itu akan muncul setelah "/"
    #max length itu limit karakternya
    price = models.DecimalField(max_digits=14, decimal_places=0)
    #desimalfield itu biar angkanya bisa ada komanya
    #max_digits menunjukkan total jumlah digit yang dapat disimpan
    #decimal_places menunjukkan berapa banyak digit yang ada di sebelah kanan titik desimal

    
    image = models.ImageField(upload_to='images/')
    #imagefield itu untuk nyimpen gambar
    #upload_to menentukan direktori di mana file gambar yang diunggah akan disimpan
    #gambar akan disimpan dalam direktori images/ yang terletak dalam direktori MEDIA_ROOT
    class Meta:
        verbose_name_plural = 'products'
    #gunanya biar pluralnya jadi "products"
    def __str__(self): #string function
        return self.title
        #return ini biar judulnya muncul, jadi bukan "title 1" tapi yang muncul nanti judulnya
    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])
    #custom url
    #args=[self.slug] adalah daftar argumen yang akan dimasukkan ke dalam pola URL, self.slug adalah nilai slug dari objek saat ini

