import os
from tabulate import tabulate

class Debitur :
    def __init__(self, nama, ktp, limit):
        self.nama = nama
        self.__ktp = ktp
        self._limit = limit
        
    @property    
    def getKTP(self) :
        return self.__ktp
    
    @property
    def getlimit(self) :
        return self._limit         
        
class Pinjaman(Debitur) :
    def __init__(self, nama, bulan, pinjaman, bunga):
        self.nama = nama
        self.bulan = bulan
        self.pinjaman = pinjaman
        self.bunga = bunga
        
    def totalAngsuran(self) :
        angsuran_pokok = self.pinjaman * (self.bunga/100)
        angsuran_bulanan = angsuran_pokok / self.bulan
        return angsuran_pokok + angsuran_bulanan
        
        
def mainMenu() :
    print("\n==================== Menu Admin Pinjol ====================")
    print("1. Kelola Debitur")
    print("2. Kelola Pinjaman")
    print("0. Keluar\n")
    
def debiturMenu() :
    print("\n====================== Menu Debitur =======================")
    print("1. Tampilkan Semua Debitur")
    print("2. Cari Debitur")
    print("3. Tambah Debitur")
    print("0. Keluar\n")
    
def pinjamanMenu() :
    print("\n====================== Menu Pinjaman =======================")
    print("1. Tambah Pinjaman")
    print("2. Tampilkan Pinjaman")
    print("0. Keluar\n")

def main() :
    header1 = ["Nama Debitur", "No. KTP", "Limit Pinjaman"]
    header2 = ["Nama Debotur", "Pinjaman", "Bunga", "Bulan", "Angsuran/bln"]
    total_debitur = [["Bouyem", 123, 5000000], ["Sukiyem", 234, 1000000], ["Tono", 345, 2000000]]
    total_pinjaman = []
    
    while True :
        try : 
            os.system("cls")
            
            mainMenu() # Tampil menu utama
            input_menu = input("Pilih Menu : ")
            if input_menu == "1" :
                while True :
                    os.system("cls")        
                    
                    debiturMenu() # Tampil menu debitur
                    input_menu = input("Pilih Menu : ")

                    if input_menu == "1" :
                        print(tabulate(total_debitur, headers=header1, tablefmt="double_outline"))
                    elif input_menu == "2" :
                        input_nama = input("Masukkan nama yang ingin dicari : ")
                        the_name = []
                        for value in total_debitur :
                            if value[0].lower() == input_nama.lower() :
                                the_name.append(value)
                                print()
                        print(tabulate(the_name, headers=header1, tablefmt="double_outline"))        
                        if the_name == [] :
                            print(f"\n{input_nama} tidak ada di daftar debitur\n")
                        the_name.clear()
                    elif input_menu == "3" :
                        input_ktp = int(input("Masukkan No. KTP Baru : "))
                        
                        for value in (total_debitur) :
                            the_ktp = []
                            if value[1] == input_ktp :
                                print(f"{input_ktp} telah terdaftar")
                                break
                        else : 
                            input_nama = input("Masukkan Nama Baru : ")
                            input_limit = int(input("Masukkan Limit Pinjaman Baru : "))
                            debitur = Debitur(input_nama, input_ktp, input_limit)
                            total_debitur.append([debitur.nama, debitur.getKTP, debitur.getlimit])
                            print(f"\nDebitur atas nama {input_nama} berhasil ditambahkan\n")
                    elif input_menu == "0" :
                        break
                            
                    os.system("pause")
            elif input_menu == "2" :            
                while True :
                    os.system("cls")
                    
                    pinjamanMenu() # Tampil menu pinjaman
                
                    input_menu = input("Pilih Menu : ")
                
                    if input_menu == "1" :
                        input_nama = input("Masukkan nama debitur : ")
                        
                        for value in total_debitur :
                            the_name = []
                            if value[0].lower() == input_nama.lower() :
                                the_name.append(value)
                                input_pinjaman = int(input("Masukkan jumlah pinjaman : Rp. "))
                                if value[2] < input_pinjaman :
                                    print("Pinjaman anda lebih besar dari limit anda")
                                    break
                                else : 
                                    input_bunga = int(input("Masukkan bunga : "))
                                    input_bulan = int(input("Masukkan limit waktu dalam bulan :  "))
                                    peminjam = Pinjaman(input_nama, input_bulan, input_pinjaman, input_bunga)
                                    total_pinjaman.append([peminjam.nama, peminjam.pinjaman, peminjam.bunga, peminjam.bulan, peminjam.totalAngsuran()])
                                    print(f"\nPinjaman atas nama {input_nama} berhasil ditambahkan\n")
                                break 
                        if the_name == [] :
                            print(f"\n{input_nama} belum terdaftar\n")
                    elif input_menu == "2" :
                        print(tabulate(total_pinjaman, headers=header2, tablefmt="double_outline"))
                    elif input_menu == "0" :
                        break
                    else : 
                        print("Pilih opsi yang tepat")
                    
                    os.system("pause")
            elif input_menu == "0" :
                break
            else : 
                print("Pilih opsi yang tepat")
            
            os.system("pause")
        except : 
            print("Mbok yo input seng bener boss")   
            os.system("pause")     

if __name__ == "__main__" :
    main()
    