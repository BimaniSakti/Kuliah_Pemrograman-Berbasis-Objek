import mysql.connector
from tabulate import tabulate
from datetime import datetime
import os
import uuid


class Pegawai:
    def __init__(self, nik:str, nama:str, alamat:str):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat


class Produk:
    def __init__(self, kode:str, nama:str, jenis:str, harga:int):
        self.kode = kode
        self.nama = nama
        self.jenis = jenis
        self.harga = harga 


def generateProductId():
    return f"P-{uuid.uuid4().hex[:5]}"

def generateNoStruk():
    return f"S-{uuid.uuid4().hex[:5]}"
    

def connectionDatabae():
    conn = mysql.connector.connect(
        port = 3306,
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'penjualan'
    )
    
    if conn.is_connected:
        return conn
    return False

def showEmployees():
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM pegawai")
        hasil = cur.fetchall()
        
        return hasil
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")
        
    finally:
        if conn.is_connected:
            cur.close()
            conn.close()

def showProducts():
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM produk")
        hasil = cur.fetchall()
        
        return hasil
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")
        
    finally:
        if conn.is_connected:
            cur.close()
            conn.close()

def showStruk(no_struk):
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute(
            """
            SELECT
            produk.nama_produk,
            transaksi.jumlah_beli,
            produk.harga_produk,
            (produk.harga_produk * transaksi.jumlah_beli) AS total_per_barang
            FROM 
            transaksi
            JOIN
            produk ON produk.kode_produk = transaksi.kode_produk
            WHERE
            transaksi.no_struk = %s
            """,
            (no_struk, )
        )
        hasil = cur.fetchall()
        
        cur.execute(
            '''
            SELECT
            no_struk,
            total_harga
            FROM
            struk
            WHERE
            no_struk = %s
            ''',
            (no_struk, )
        )
        total_harga = cur.fetchone()[1]
        
        return hasil, total_harga
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")
        
    finally:
        if conn.is_connected:
            cur.close()
            conn.close()
            
def showAllStruk():
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute("SELECT struk.no_struk, struk.tanggal, struk.total_harga, pegawai.nama_pegawai FROM struk JOIN pegawai ON pegawai.nik = struk.nik")
        hasil = cur.fetchall()
        
        return hasil
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")
        
    finally:
        if conn.is_connected:
            cur.close()
            conn.close()

def inputEmployee(pegawai:object):
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute("INSERT INTO pegawai VALUES (%s, %s, %s)", (pegawai.nik, pegawai.nama, pegawai.alamat))
        conn.commit()
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")

    finally:
        if conn.is_connected:
            cur.close()
            conn.close()

def inputProduct(produk:object):
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute("INSERT INTO produk VALUES (%s, %s, %s, %s)", (produk.kode, produk.nama, produk.jenis, produk.harga))
        conn.commit()
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")

    finally:
        if conn.is_connected:
            cur.close()
            conn.close()
            
def inputStruk(no_struk:str, tanggal:str, nama_pegawai:str):
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute(
            """
            SELECT
            nik
            FROM
            pegawai
            WHERE
            nama_pegawai=%s
            """,
            (nama_pegawai, )
        )
        nik = cur.fetchone()[0]
        
        cur.execute("INSERT INTO struk (no_struk, tanggal, nik) VALUES (%s, %s, %s)", (no_struk, tanggal, nik))
        conn.commit()
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")

    finally:
        if conn.is_connected:
            cur.close()
            conn.close()
            
def inputTransaction(no_struk:str, nama_produk:str, jumlah_beli:int):
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute(
            """
            SELECT
            kode_produk
            FROM
            produk
            WHERE
            nama_produk=%s
            """,
            (nama_produk, )
        )
        kode_produk = cur.fetchone()[0]
        
        cur.execute("INSERT INTO transaksi VALUES (%s, %s, %s)", (no_struk, kode_produk, jumlah_beli))
        conn.commit()
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")

    finally:
        if conn.is_connected:
            cur.close()
            conn.close()
            
def updateTotalPrice(no_struk:str):
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute(
            """
            SELECT
            SUM(transaksi.jumlah_beli * produk.harga_produk) AS total_harga
            FROM 
            transaksi
            JOIN 
            produk ON produk.kode_produk = transaksi.kode_produk
            WHERE
            transaksi.no_struk=%s
            """, (no_struk, ))
        total_harga = cur.fetchone()[0]
        
        cur.execute("UPDATE struk SET total_harga=%s WHERE no_struk=%s", (total_harga, no_struk))
        conn.commit()
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")

    finally:
        if conn.is_connected:
            cur.close()
            conn.close()

def editEmployee(nik_baru:str, nama_baru:str, alamat_baru:str, nik_lama:str):
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute("UPDATE pegawai SET nik=%s, nama_pegawai=%s, alamat_pegawai=%s WHERE nik=%s", (nik_baru, nama_baru, alamat_baru, nik_lama))
        conn.commit()
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")

    finally:
        if conn.is_connected:
            cur.close()
            conn.close()
            
def editProduct(nama_baru:str, jenis_baru:str, harga_baru:str, kode_lama:str):
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute("UPDATE produk SET nama_produk=%s, jenis_produk=%s, harga_produk=%s WHERE kode_produk=%s", (nama_baru, jenis_baru, harga_baru, kode_lama))
        conn.commit()
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")

    finally:
        if conn.is_connected:
            cur.close()
            conn.close()

def deleteEmployee(nik_lama):
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute("DELETE FROM pegawai WHERE nik=%s", (nik_lama, ))
        conn.commit()
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")

    finally:
        if conn.is_connected:
            cur.close()
            conn.close()

def deleteProduct(kode_lama):
    try:
        conn = connectionDatabae()
        cur = conn.cursor()
        
        cur.execute("DELETE FROM produk WHERE kode_produk=%s", (kode_lama, ))
        conn.commit()
        
    except mysql.connector.Error as ERROR:
        print(f"Terjadi Kesalahan: {ERROR}")

    finally:
        if conn.is_connected:
            cur.close()
            conn.close()

def menu():
    print("========== Supermarket ==========")
    print("1. Tampilkan data pegawai")
    print("2. Tampilkan data produk")
    print("3. Tampilkan semua struk")
    print("4. Input data pegawai")
    print("5. Input data produk")
    print("6. Edit data pegawai")
    print("7. Edit data produk")
    print("8. Hapus data pegaawai")
    print("9. Hapus data produk")
    print("10. jual produk")
    print("0. Keluar\n")
    
def main():
    header_pegawai = ["NIK", "Nama", "Alamat"]
    header_produk = ["Kode", "Nama", "Jenis", "Harga"]
    header_struk = ["Nomor Struk", "Tanggal", "Total Pembayaran", "Nama Pegawai"]
    
    while True:
        # clear terminal
        os.system("cls")
        
        # panggil Menu Utama
        menu() 
        
        # pilih menu
        input_menu = input("Pilih Menu : ")
        
        # menu tampilkan semua pegawai
        if input_menu == "1" :
            list_pegawai = showEmployees()
            if list_pegawai:
                print(tabulate(list_pegawai, headers=header_pegawai, tablefmt="double_outline"))
            else:
                print("Tidak ada pegawai\n")
            
        # menu tampilkan semua produk
        elif input_menu == "2" :
            list_produk = showProducts()
            if list_produk:
                print(tabulate(list_produk, headers=header_produk, tablefmt="double_outline"))
            else:
                print("Tidak ada produk\n")
                
        elif input_menu == "3":
            list_struk = showAllStruk()
            if list_struk:
                print(tabulate(list_struk, headers=header_struk, tablefmt="double_outline"))
            else:
                print("Tidak ada struk\n")
            
        # menu input data pegawai
        elif input_menu == "4" :
            nik = input("Masukkan NIK anda: ")
            nama = input("Masukkan nama anda: ")
            alamat = input("Masukkan alamat anda: ")
            pegawai_baru = Pegawai(nik, nama, alamat)
            inputEmployee(pegawai_baru)
            print(f"Pegawai atas nama {nama} berhasil direkrut\n")

        # menu input data produk
        elif input_menu == "5":
            list_pegawai = showEmployees()
            kode_produk = generateProductId()
            nama_produk = input("Masukkan nama produk: ")
            jenis_produk = input("Masukkan jenis produk: ")
            harga_produk = input("Masukkan harga produk: ")
            produk_baru = Produk(kode_produk, nama_produk, jenis_produk, harga_produk)
            inputProduct(produk_baru)
            print(f"Produk {nama_produk} berhasil ditambahkan\n")
        
        # menu edit data pegawai
        elif input_menu == "6":
            list_pegawai = showEmployees()
            nik_lama = input("Masukkan NIK anda yang lama: ")
            cek_nik_lama = next((pegawai for pegawai in list_pegawai if pegawai[0] == nik_lama), None)
            if cek_nik_lama:
                nama = input("Masukkan nama baru anda: ")
                alamat = input("Masukkan alamat baru anda: ")
                nik_baru = input("Masukkan NIK baru anda: ")
                editEmployee(nik_baru, nama, alamat, nik_lama)
                print(f"Pegawai atas nama {cek_nik_lama[1]} berhasil diubah menjadi {nama}\n")   
            else:
                print(f"{nik_lama} tidak ditemukan\n")
        
        # menu edit data produk
        elif input_menu == "7":
            list_produk = showProducts()
            kode_produk_lama = input("Masukkan kode produk yang lama: ")
            cek_kode_produk = next((produk for produk in list_produk if produk[0] == kode_produk_lama), None)
            if cek_kode_produk:
                nama_produk_baru = input("Masukkan nama produk yang baru: ")
                jenis_produk_baru = input("Masukkan jenis produk yang baru: ")
                harga_produk_baru = input("Masukkan harga produk yang baru: Rp ")
                editProduct(nama_produk_baru, jenis_produk_baru, harga_produk_baru, kode_produk_lama)
                print(f"Produk {cek_kode_produk[1]} berhasil diubah menjadi {nama_produk_baru}\n")   
            else:
                print(f"{kode_produk_lama} tidak ditemukan\n")
        
        # menu hapus data pegawai
        elif input_menu == "8":
            list_pegawai = showEmployees()
            nik = input("Masukkan NIK yang ingin dihapus: ")
            cek_nik = next((pegawai for pegawai in list_pegawai if pegawai[0] == nik), None)
            if cek_nik:
                deleteEmployee(nik)
                print(f"Pegawai dengan NIK {nik} berhasil dipecat\n")
            else:
                print(f"{nik} tidak ditemukan\n")
        
        # menu hapus data produk 
        elif input_menu == "9":
            list_produk = showProducts()
            kode_produk = input("Masukkan kode produk yang ingin dihapus: ")
            cek_kode_produk = next((produk for produk in list_produk if produk[0] == kode_produk), None)
            if cek_kode_produk:
                deleteProduct(kode_produk)
                print(f"Produk dengan kode {kode_produk} berhasil dihapus\n")
            else:
                print(f"{kode_produk} tidak ditemukan\n")
        
        # menu jual produk dan langsung tampilkan struk
        elif input_menu == "10":
            try:
                list_pegawai = showEmployees()
                list_produk = showProducts()
                nama_pegawai = input("Masukkan nama pegawai: ")
                no_struk = generateNoStruk() 
                tanggal = datetime.now().strftime("%H-%M-%S %d/%m/%Y")
                inputStruk(no_struk, tanggal, nama_pegawai)
                while True:
                    nama_produk = input("Masukkan nama produk yang ingin dibeli: ")
                    if nama_produk not in [produk[1] for produk in list_produk]:
                        continue
                    while True:
                        try:
                            jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))
                            if jumlah_beli <= 0:
                                continue
                            break
                        except ValueError:
                            print("Jumlah Harus berupa angka\n")
                    inputTransaction(no_struk, nama_produk, jumlah_beli)
                    pesan_lagi = input("Apakah ingin membeli produk lain? [Y/N]: ")
                    if pesan_lagi.upper() == "N":
                        break
                updateTotalPrice(no_struk)
                detail_struk, total_harga = showStruk(no_struk) 
                # Cetak Struk
                print()
                print("=" * 40)
                print(f"{'STRUK PEMBAYARAN':^40}")
                print("=" * 40)
                print(f"No Struk: {no_struk}")
                print("-" * 40)
                print(f"{'Barang':<15} {'Jumlah':<7} {'Harga':<10} {'Total':<10}")
                print("-" * 40)
                for item in detail_struk:
                    nama_produk = item[0]
                    jumlah_beli = item[1]
                    harga_produk = item[2]
                    total_per_barang = item[3]
                    print(f"{nama_produk:<15} {jumlah_beli:<7} {harga_produk:<10} {total_per_barang:<10}")
                print("-" * 40)
                print(f"{'Total Pembayaran':<34} {total_harga}")
                print("=" * 40)
                print()
            except TypeError:
                print("\nTerjadi Kesalahan: terdapat kesalahan pengetikan\n")
                
        # keluar
        elif input_menu == "0":
            break
        
        # pilihan menu salah
        else:
            print("\nPilihan tidak ada di menu\n")

        # pause terminal
        os.system("pause")


if __name__ == "__main__":
    main()