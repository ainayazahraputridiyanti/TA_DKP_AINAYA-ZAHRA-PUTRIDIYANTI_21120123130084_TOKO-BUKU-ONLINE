#konfigurasi admin di Django untuk model Category dan Product
#ini memungkinkan pengelolaan model-model tersebut melalui antarmuka admin Django

from django.contrib import admin #mengimpor modul admin dari Django, yang memungkinkan untuk mengelola model melalui antarmuka admin Django
from.models import Category, Product #mengimpor model Category dan Product dari file models.py

@admin.register(Category) #memberitahu Django untuk mendaftarkan model Category dengan konfigurasi yang ditentukan dalam kelas CategoryAdmin
class CategoryAdmin(admin.ModelAdmin): #mendefinisikan konfigurasi khusus untuk bagaimana model Category ditampilkan di admin
    prepopulated_fields = {'slug': ('name',)} #saat memberi nama kategori di admin, slug akan otomatis mengikuti nama tersebut

@admin.register(Product) #memberitahu Django untuk mendaftarkan model Product dengan konfigurasi yang ditentukan dalam kelas ProductAdmin
class ProductAdmin(admin.ModelAdmin): #mendefinisikan konfigurasi khusus untuk bagaimana model Product ditampilkan di admin
    prepopulated_fields = {'slug': ('title',)} #saat memberi judul produk di admin, slug akan otomatis mengikuti judul tersebut

#gunanya itu kalo misalkan nulis nama di category
#nanti slugnya langsung ketulis sama persis kayak namanya

