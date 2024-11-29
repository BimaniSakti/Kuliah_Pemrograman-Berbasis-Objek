import uuid
import os
from copy import deepcopy


class Order :
    def __init__(self):
        self._id = None
        self.name = None
        self.quantity = None
        self.info = "Belum Terkirim"
        
    def setOrder(self, name:str, quantity:int) :
        self._id = self.generate_id()
        self.name = name
        self.quantity = quantity
        
    def updateInfo(self) :
        self.info = "Sudah Terkirim"
    
    @staticmethod
    def generate_id():
        return str(uuid.uuid4())[:5]

class Delivery :
    def __init__(self, courier:str, date:str, address:str):
        self._id = self.generate_id()
        self.courier = courier
        self.date = date
        self.address = address

    def infoCourier(self) :
        print("Info Kurir")
        print(f"{self.courier}  | {self.date}   | {self.address}    ")
    
    @staticmethod
    def generate_id():
        return str(uuid.uuid4())[:5]


def mainMenu() :
    print("\n==========================")
    print("1. Pesanan")
    print("2. Kurir")
    print("0. Exit\n")
    
def subMenuOrder() :
    print("\n==========================")
    print("1. Buat Pesanan")
    print("2. Status Pesanan")
    print("0. Exit\n")
    
def subMenuDelivery() :
    print("\n==========================")
    print("1. Ambil Pesanan")
    print("2. Update Info Pesanan")
    print("0. Exit\n")

def main() :
    list_order = []
    list_take = []
    
    while True :
        os.system('cls')

        mainMenu()
        input_menu = input("Pilih Menu : ")
        if input_menu == "1" :
            while True :
                os.system('cls')
                subMenuOrder()
                input_menu = input("Pilih Menu : ")
                if input_menu == "1" :
                    name_stuff = input("Nama Barang : ")
                    qty_stuff = input("Jumlah Barang : ")
                    order = Order()
                    order.setOrder(name_stuff, qty_stuff)
                    list_order.append([order._id, order.name, order.quantity, order.info])
                elif input_menu == "2" :
                    name_stuff = input("Nama Barang : ")
                    for i in list_order :
                        if list_order and i[1] == name_stuff :    
                            print(f"barang {name_stuff} {i[3]}")
                            break
                elif input_menu == "0" :
                    break
                else :
                    print("Pilih opsi yang tepat")
                os.system("pause")
        elif input_menu == "2" :
            while True :
                os.system('cls')
                subMenuDelivery()
                input_menu = input("Pilih Menu : ")
                if input_menu == "1" :
                    name = input("Nama Kurir : ")
                    date = input("Tanggal : ")
                    address = input("Alamat : ")
                    deliver = Delivery(name, date, address) 
                    deliver.infoCourier()
                    list_take = deepcopy(list_order)
                    list_order.clear()
                elif input_menu == "2" :
                    name_stuff = input("Nama Barang : ")
                    order.updateInfo()
                    for i in list_order :
                        i[3] = order.info
                    for i in list_take :
                        if i[1] == name_stuff :    
                            print(f"barang {name_stuff} {i[3]}")
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
        
if __name__ == "__main__" :
    main()