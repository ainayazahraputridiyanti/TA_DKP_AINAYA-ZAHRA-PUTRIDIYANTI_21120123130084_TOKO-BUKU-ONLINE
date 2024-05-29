#mengatur pengaturan dasar untuk aplikasi "store" dalam proyek Django,
#memastikan bahwa aplikasi tersebut dikenali dan dikonfigurasi dengan benar oleh Django
#mendefinisikan pengaturan untuk aplikasi yang bernama "store"

from django.apps import AppConfig
#mengimpor kelas AppConfig dari modul django.apps
#AppConfig adalah kelas dasar yang digunakan untuk mengkonfigurasi aplikasi Django
class StoreConfig(AppConfig):
#mendefinisikan kelas StoreConfig yang diwariskan dari AppConfig
#kelas ini digunakan untuk mengkonfigurasi aplikasi "store"
    default_auto_field = 'django.db.models.BigAutoField'
    #menentukan tipe field otomatis default yang akan digunakan untuk primary key di model-model dalam aplikasi ini
    #BigAutoField=tipe field yang menghasilkan angka integer besar secara otomatis untuk primary key
    #bermanfaat untuk proyek yang memerlukan banyak data dan menghindari kemungkinan overflow pada integer kecil
    name = 'store'
    #menentukan nama aplikasi
