import os
from tabulate import tabulate
from uuid import uuid4


class Pegawai:
    def __init__(self, nik, nama, alamat):
        self._nik = nik
        self.nama = nama
        self.alamat = alamat
        
    def purchase(self, produk, jumlah_produk):
        no_transaksi = f"T-{self._nik}-{produk._kode_produk}"
        total_harga = jumlah_produk * produk.harga
        struk = Struk(no_transaksi, self.nama, produk.nama_produk, jumlah_produk, total_harga)
        return struk


class Transaksi:
    def __init__(self, no_transaksi, detail_transaksi):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = detail_transaksi
        
        
class Struk:
    def __init__(self, no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga):
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.nama_produk = nama_produk
        self.jumlah_produk = jumlah_produk
        self.total_harga = total_harga
        
    def displayStruck(self):
        print(f"No Transaksi    : {self.no_transaksi}\n"
                f"Nama Pegawai  : {self.nama_pegawai}\n"
                f"Nama Produk   : {self.nama_produk}\n"
                f"Jumlah Produk : {self.jumlah_produk}\n"
                f"Total Harga   : {self.total_harga}")
        

class Produk:
    def __init__(self, kode_produk, nama_produk, jenis_produk):
        self._kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        
    def editProduct(self, nama_produk, jenis_produk) :
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk


class Snack(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk)
        self.harga = harga
        
    def editProduct(self, nama_produk, jenis_produk, harga) :
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga
        
        
class Makanan(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk)
        self.harga = harga

    def editProduct(self, nama_produk, jenis_produk, harga) :
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga

        
class Minuman(Produk):
    def __init__(self, kode_produk, nama_produk, jenis_produk, harga):
        super().__init__(kode_produk, nama_produk, jenis_produk)
        self.harga = harga
        
    def editProduct(self, nama_produk, jenis_produk, harga) :
        self.nama_produk = nama_produk
        self.jenis_produk = jenis_produk
        self.harga = harga


def generate_id():
    return str(uuid4())[:5]

def mainMenu():
    print("============================")
    print("1. Data pegawai")
    print("2. Beli produk")
    print("3. Olah Produk")
    print("0. Keluar\n")
    
def subMenuProduk():
    print("============================")
    print("1. Tambah Produk")
    print("2. Edit Produk")
    print("3. Hapus Produk")
    print("4. Tampil Semua Produk")
    print("0. Keluar\n")
    
def appendProduct(kode_produk, nama_produk, jenis_produk, harga_produk, list_produk):
    cek_class = {
        'snack' : Snack,
        'makanan' : Makanan,
        'minuman' : Minuman
    }
    class_produk = cek_class.get(jenis_produk.lower())
    if class_produk: 
        produk = class_produk(kode_produk, nama_produk, jenis_produk, harga_produk)
        list_produk.append([
        produk._kode_produk, 
        produk.nama_produk, 
        produk.jenis_produk, 
        produk.harga
        ])
        print(f"{produk.nama_produk} Telah ditambahkan")
    else :
        print("Terjadi kesalahan")

# def updateProduct(nama_produk, jenis_produk, harga_produk, list_produk):
    
    
def main():
    alucard = Pegawai("5230411296", "alucard", "Kulon Progo")
    gusion = Pegawai("5230411290", "Gusion", "Magelang")
    balmond = Pegawai("5230411277", "Balmond", "Mlati")
    irfan = Pegawai("5230411322", "irfan", "Kulon Progo")
    moskov = Pegawai("5230411292", "moskov", "Yogyakarta")
    header_pegawai = ["NIK", "Nama", "Alamat"]
    list_pegawai = [[alucard._nik, alucard.nama, alucard.alamat], [gusion._nik, gusion.nama, gusion.alamat], [balmond._nik, balmond.nama, balmond.alamat], [irfan._nik, irfan.nama, irfan.alamat], [moskov._nik, moskov.nama, moskov.alamat]]
    
    nasgor = Makanan("Sweop", "Nasi Goreng", "Makanan", 10000)
    header_produk = ["Kode", "Nama", "Jenis", "Harga"]
    list_produk = [[nasgor._kode_produk, nasgor.nama_produk, nasgor.jenis_produk, nasgor.harga]]
    
    
    while True:
        os.system("cls")
        
        # Panggil Menu Utama
        mainMenu() 
        
        input_menu = input("Pilih Menu : ")
        if input_menu == "1" :
            print(tabulate(list_pegawai, headers=header_pegawai, tablefmt="double_outline"))
        # elif input_menu == "2" :
        elif input_menu == "3" :
            while True:
                os.system("cls")
                
                subMenuProduk()
                
                input_menu = input("Pilih Menu : ")
                if input_menu == "1" :
                    kode_produk = generate_id()
                    nama_produk = input("Masukkan nama produk   : ")
                    jenis_produk = input("Masukkan jenis produk [snack, makanan, minuman]  : ")
                    harga_produk = input("Masukkan harga produk   : ")
                    appendProduct(kode_produk, nama_produk, jenis_produk, harga_produk, list_produk)
                elif input_menu == "2":
                    nama_produk_lama = input("Masukkan nama produk yang lama : ")
                    cek_nama_produk = None
                    for produk in list_produk:
                        if produk[1].lower() == nama_produk_lama.lower() :
                            cek_nama_produk = nama_produk_lama
                            break
                    if cek_nama_produk == nama_produk_lama :    
                        nama_produk_baru = input("Masukkan nama produk yang baru : ")
                        jenis_produk = input("Masukkan jenis produk [snack, makanan, minuman]  : ")
                        harga_produk = input("Masukkan harga produk   : ")
                        if jenis_produk.lower() == "snack":
                            snack = Snack(kode_produk, nama_produk_baru, jenis_produk, harga_produk)
                            print(f"{snack.nama_produk} Telah ditambahkan")
                        elif jenis_produk.lower() == "makanan":
                            makanan = Makanan(kode_produk, nama_produk_baru, jenis_produk, harga_produk)
                            print(f"{makanan.nama_produk} Telah ditambahkan")
                        elif jenis_produk.lower() == "minuman":
                            minuman = Minuman(kode_produk, nama_produk_baru, jenis_produk, harga_produk)
                            print(f"{minuman.nama_produk} Telah ditambahkan")
                        else :
                            print("Terjadi kesalahan")
                    else :
                        print("Barang tidak ditemukan")
                elif input_menu == "3":
                    nama_produk = input("Masukkan nama produk yang lama : ")
                    cek_nama_produk = None
                    for produk in list_produk:
                        if produk[1].lower() == nama_produk.lower() :
                            cek_nama_produk = nama_produk
                            list_produk.remove(produk)
                            print(f"{nama_produk} berhasil dihapus")                
                            break
                    if cek_nama_produk == None :
                        print("Barang tidak ditemukan")
                elif input_menu == "4":
                    print(tabulate(list_produk, headers=header_produk, tablefmt="double_outline"))
                else : 
                    print("Pilih menu yang tepat")
                    
                os.system("pause")
        elif input_menu == "0":
            print("Terimakasih")
            break
        else : 
            print("Pilih menu yang tepat")
        
        
        os.system("pause")


if __name__ == "__main__":
    main()