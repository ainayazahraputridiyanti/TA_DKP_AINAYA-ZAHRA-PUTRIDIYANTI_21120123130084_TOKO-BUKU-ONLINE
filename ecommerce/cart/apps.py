#mengatur pengaturan dasar untuk aplikasi "cart" dalam proyek Django,
#memastikan bahwa aplikasi tersebut dikenali dan dikonfigurasi dengan benar oleh Django
#mendefinisikan pengaturan untuk aplikasi yang bernama "cart"

from django.apps import AppConfig
#mengimpor kelas AppConfig dari modul django.apps
#AppConfig adalah kelas dasar yang digunakan untuk mengkonfigurasi aplikasi Django

class CartConfig(AppConfig):
#mendefinisikan kelas CartConfig yang diwariskan dari AppConfig
#kelas ini digunakan untuk mengkonfigurasi aplikasi "cart"
    default_auto_field = 'django.db.models.BigAutoField'
    #menentukan tipe field otomatis default yang akan digunakan untuk primary key di model-model dalam aplikasi ini
    #BigAutoField=tipe field yang menghasilkan angka integer besar secara otomatis untuk primary key
    #bermanfaat untuk proyek yang memerlukan banyak data dan menghindari kemungkinan overflow pada integer kecil
    name = 'cart'
    #menentukan nama aplikasi
    