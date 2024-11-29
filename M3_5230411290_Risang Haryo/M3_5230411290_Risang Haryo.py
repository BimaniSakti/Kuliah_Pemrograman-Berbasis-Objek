import os

class MenuList :
    def __init__(self) -> None:
        self.name = None
        self.price = None   
    
    def insert(self, name, price) :
        self.name = name
        self.price = price

    def display(self) :
        print(F"{self.name}\t\t\t {self.price}")

def mainMenu() :
    print("\n===== Choose menu =====")
    print("1. Look for Foods")
    print("2. Look for Beverages")
    print("3. Insert Food or Beverages")
    print("0. Exit\n")

def subMenu() :
    print("\n===== Insert =====")
    print("1. Foods")
    print("2. Beverages")
    print("0. Exit\n")

def main() :
    total_foods = []
    total_beverages = []    
    while True :
        menu = MenuList()
        os.system("cls")

        mainMenu() # Panggil menu utama
        input_menu = input("Choose menu : ")
        match input_menu :
            case "1" : 
                if total_foods == [] :
                    print("There is no food\n")
                else :
                    print("Nama\t\t\t Harga")
                    for i in total_foods :
                        i.display()
            case "2" :
                if total_beverages == [] :
                    print("There is no beverage\n")
                else : 
                    print("Nama\t\t\t Harga")
                    for i in total_beverages :
                        i.display()
            case "3" :
                while True :
                    try :
                        os.system("cls")

                        subMenu() # Panggil sub menu tambah makanan atau minuman
                        input_menu = input("Choose menu : ")
                        match input_menu :
                            case "1" :
                                name = input("Insert the name of food : ")
                                price = int(input("Insert the price of food : "))
                                menu.insert(name, price)
                                total_foods.append(menu)
                                print("Pesanan berhasil ditambahkan\n")
                                break
                            case "2" :
                                name = input("Insert the name of beverage : ")
                                price = int(input("Insert the price of beverage : "))
                                menu.insert(name, price)
                                total_beverages.append(menu)
                                print("Pesanan berhasil ditambahkan\n")
                                break
                            case "0" :
                                break
                            case _ :
                                print("Choose the menu correctly!\n")
                                os.system("pause")
                                continue
                    except :
                        print("Pesanan gagal ditambahkan\n")
                        os.system("pause")
                        continue
            case "0" :
                break
            case _ :
                print("Choose the menu correctly!\n")
        
        os.system("pause")

if __name__ == "__main__" :
    main()