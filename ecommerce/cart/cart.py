#mendefinisikan kelas Cart untuk mengelola keranjang belanja dalam sebuah aplikasi e-commerce
#mencakup fungsi seperti menambahkan, menghapus, dan memperbarui item, menghitung total harga, dan jumlah item dalam keranjang

#mengimpor kelas Decimal dari modul decimal untuk menangani perhitungan finansial yang memerlukan presisi
from decimal import Decimal

#mengimpor model Product dari aplikasi store untuk mengakses informasi produk
from store.models import Product

#Bikin kelas Cart
class Cart():

#method init menangani sesi keranjang belanja yang akan dipanggil saat membuat objek Cart
    def __init__(self, request):
        #tempat penyimpanan data keranjang belanja sementara
        self.session = request.session 
        # Returning user - obtain his/her existing session
        #mengambil data keranjang belanja dari sesi pengguna, jika ada
        cart = self.session.get('session_key')
        # New user - generate a new session
        #memeriksa apakah pengguna baru, jika ya, membuat sesi baru untuk mereka
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        #disimpan di var self cart, bisa diakses oleh metode lain dalam kelas cart
        self.cart = cart

#method add  buat nambahin produk ke cart
    def add(self, product, product_qty):
        #mengambil ID produk, mengonversinya menjadi teks (string), dan menyimpannya dalam variabel product_id
        product_id = str(product.id)
        #memeriksa produk sudah ada di dalam keranjang belanja atau tidak
        if product_id in self.cart:
            #kalo ada, mengupdate jumlah produk dalam keranjang belanja dengan jumlah yang baru
            self.cart[product_id]['qty'] = product_qty
        #kalo engga, nanti akan menambahkan produk baru ke dalam keranjang belanja, ada harga dan jumlah produknya
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}
        #tanda sesi telah dimodifikasi, jadi perubahan akan disimpan ketika sesinya disimpan kembali
        self.session.modified = True

#method delete buat hapus di cart
#menghapus produk dari keranjang jika produk ada, dan memastikan sesi pengguna diperbarui untuk mencerminkan perubahan
    def delete(self, product):
        #mengubah ID produk menjadi string untuk digunakan sebagai kunci dalam keranjang.
        product_id = str(product)
        #memeriksa apakah produk dengan product_id ada dalam keranjang (self.cart), jika ada, produk dihapus dari keranjang
        if product_id in self.cart:
            del self.cart[product_id]
        ##menandai bahwa sesi pengguna telah dimodifikasi, sehingga perubahan dalam keranjang belanja akan disimpan
        self.session.modified = True

#method update buat memperbarui jumlah di cart
#memperbarui kuantitas suatu produk dalam keranjang jika ada, dan memastikan sesi pengguna diperbarui untuk mencerminkan perubahan
    def update(self, product, qty):
        #mengubah ID produk menjadi string untuk digunakan sebagai kunci dalam keranjang
        product_id = str(product)
        #menyimpan kuantitas produk yang diberikan sebagai parameter qty
        product_quantity = qty
        #memeriksa apakah produk dengan product_id ada dalam keranjang (self.cart)
        #jika ada, kuantitas produk tersebut diperbarui dengan nilai product_quantity
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_quantity
        #menandai bahwa sesi pengguna telah dimodifikasi, sehingga perubahan dalam keranjang belanja akan disimpan
        self.session.modified = True

#method len buat mengembalikan total jumlah semua item dalam keranjang belanja
#menghitung dan mengembalikan total jumlah semua item dalam keranjang belanja dengan menjumlahkan kuantitas setiap item
    def __len__(self):
        #melakukan perhitungan total kuantitas semua item dalam keranjang belanja dan mengembalikan hasilnya
        return sum(item['qty'] for item in self.cart.values())
        #self.cart diasumsikan sebagai dictionary yang menyimpan item-item keranjang belanja
        #menjumlahkan semua nilai yang dihasilkan ekspresi generator yang iterasi melalui setiap item
        #untuk setiap item, mengambil nilai dari kunci 'qty', yaitu kuantitas item tersebut

#method iter buat menghitung jumlah elemen
#menambahkan objek produk ke setiap item dalam keranjang, menghitung harga totalnya, dan mengembalikan item-item yang telah dilengkapi
    def __iter__(self):
        #mengambil semua kunci (ID produk) dari dictionary self.cart.
        all_product_ids = self.cart.keys()
        #mengambil objek Product dari database yang ID-nya ada dalam all_product_ids menggunakan query filter
        products = Product.objects.filter(id__in=all_product_ids)
        #membuat salinan keranjang
        import copy
        #membuat salinan mendalam (deep copy) dari keranjang belanja untuk menghindari perubahan pada keranjang asli
        cart = copy.deepcopy(self.cart)
        #untuk setiap produk yang ditemukan di database,
        for product in products:
            #tambahkan objek produk tersebut ke dalam item keranjang yang sesuai berdasarkan ID produk
            cart[str(product.id)]['product'] = product
        #mulai iterasi melalui setiap item dalam keranjang yang telah diperbarui.
        for item in cart.values():
            #define price
            #mengonversi harga item menjadi objek decimal untuk perhitungan yang lebih akurat
            item['price'] = Decimal(item['price'])
            #calculate price and qty
            #menghitung harga total per item berdasarkan harga satuan dan kuantitasnya
            item['total'] = item['price'] * item['qty']
            #final price
            #menghasilkan (yield) item dengan informasi yang telah dilengkapi ke luar metode ini
            #memungkinkan iterasi melalui item-item keranjang di luar metode iter
            yield item    

#method untuk menghitung total, jumlah x harga
#menghitung total nilai semua item dalam keranjang belanja dengan mengalikan harga dan kuantitas setiap item, dan kemudian menjumlahkan hasilnya.
    def get_total(self):
        #melakukan iterasi melalui setiap item dalam keranjang belanja
        #memastikan harga adalah bilangan desimal dan mengalikan harga setiap item dengan kuantitasnya
        #menjumlahkan hasil perkalian harga dan kuantitas setiap item
        #mengembalikan total nilai dari semua item dalam keranjang belanja
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())




  


