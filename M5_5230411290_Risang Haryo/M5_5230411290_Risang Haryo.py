import os
from tabulate import tabulate

class Music :
    header = ["Judul Musik", "Penyanyi", "Genre"]
    
    def __init__(self):
        self.title = None
        self.singer = None
        self.genre = None


class EnglishSong(Music) :
    english_songs = [["Unstoppable","Sia","E-Song"],["Dancin","Aaron Smith","E-Song"],["Fairytale","Alexander Rybak","E-Song"],["Snap","Rosa Linn","E-Song"],["Dandelions","Ruth-B","E-Song"]]
    
    def __init__(self):
        super().__init__()
        
    def display(self) :
        print(tabulate(self.english_songs, headers=self.header, tablefmt="double_outline"))
        
    def add(self, title, singer) :
        self.title = title
        self.singer = singer
        self.genre = "E-Song"
        self.english_songs.append([self.title, self.singer, self.genre])
        
    def delete(self, title):
        for song in self.english_songs :
            if song[0].lower() == title.lower() :
                self.english_songs.remove(song)
                return True
            
    def getSongs(self) :
        return self.english_songs


class ArabicSong(Music) :
    arabic_songs = [["Rahmatun Lil'Alameen","Maher Zain","A-Song"],["Ya Nabi Salam 'Alayka","Maher Zain","A-Song"],["Insha Allah","Maher Zain","A-Song"],["Baraka Allahu Lakuma","Maher Zain","A-Song"],["Thank You Allah","Maher Zain","A-Song"]]
    
    def __init__(self):
        super().__init__()
    
    def display(self) :
        print(tabulate(self.arabic_songs, headers=self.header, tablefmt="double_outline"))
    
    def add(self, title, singer) :
        self.title = title
        self.singer = singer
        self.genre = "E-Song"
        self.arabic_songs.append([self.title, self.singer, self.genre])
    
    def delete(self, title) :
        for song in self.arabic_songs :
            if song[0].lower() == title.lower() :
                self.arabic_songs.remove(song)
                return True
    
    def getSongs(self) :
        return self.arabic_songs


class JapaneseSong(Music) :
    japanase_songs = [["Nandemonaiya","Radwimps","J-Song"],["Rokudenashi","One Voice","J-Song"],["Inferno","Mrs. Green Apple","J-Song"],["Kokoronashi","Gumi","J-Song"],["Amanojaku","Gumi","J-Song"]]
    
    def __init__(self):
        super().__init__()
        
    def display(self) :
        print(tabulate(self.japanase_songs, headers=self.header, tablefmt="double_outline"))
        
    def add(self, title, singer) :
        self.title = title
        self.singer = singer
        self.genre = "E-Song"
        self.japanase_songs.append([self.title, self.singer, self.genre])
        
    def delete(self, title) :
        for song in self.japanase_songs :
            if song[0].lower() == title.lower() :
                self.japanase_songs.remove(song)
                return True
            
    def getSongs(self) :
        return self.japanase_songs


def mainMenu() :
    print("\n============= Playlist Music =============")
    print("1. English Song")
    print("2. Arabic Song")
    print("3. Japanase Song")
    print("4. Display All")
    print("5. Search Music")
    print("0. Exit\n")
    
def genreMenu(genre) :
    print(f"\n============= {genre} Song =============")
    print("1. Display Song")
    print("2. Add Song")
    print("3. Delete Song")
    print("0. Exit\n")
    
def genreMenuFunc(genre:str, obj_genre) :
    while True :
        os.system("cls")
        genreMenu(genre) # Panggil menu English song
        
        choose_menu = input("Pilih menu : ")
        if choose_menu == "1" :
            obj_genre.display()    
        elif choose_menu == "2" :
            title = input("Masukkan judul lagu yang ingin ditambahkan: ")
            singer = input("Masukkan nama penyanyi : ")
            obj_genre.add(title, singer)
            print(f"Lagu {title} berhasil ditambahkan")
        elif choose_menu == "3" :
            title = input("Masukkan judul lagu yang ingin dihapus : ")
            is_deleted = obj_genre.delete(title)
            if is_deleted == True :
                print(f"Lagu {title} berhasil dihapus")
            else : 
                print(f"Lagu {title} tidak ditemukan")
        elif choose_menu == "0" :
            break
        else :
            print("pilih opsi yang tepat")
        
        os.system("pause")
    
def main() :
    while True :
        header = ["Judul Musik", "Penyanyi", "Genre"]
        os.system("cls")
        mainMenu() # Panggil menu utama
        
        english = EnglishSong()
        arabic = ArabicSong()
        japanese = JapaneseSong()
        
        choose_menu = input("Pilih menu : ")
        if choose_menu == "1" :
            genreMenuFunc("English", english)    
        elif choose_menu == "2" :
            genreMenuFunc("Arabic", arabic)
        elif choose_menu == "3" :
            genreMenuFunc("Japanase", japanese)
        elif choose_menu == "4" :
            total_songs = english.getSongs() + arabic.getSongs() + japanese.getSongs()
            sorted_songs = sorted(total_songs, key=lambda song:song[0])
            print(tabulate(sorted_songs, headers=header, tablefmt="double_outline"))
        elif choose_menu == "5" :
            search_song = input("Cari lagu berdasarkan nama penyanyi : ")
            search_list = [i for i in total_songs if i[1].lower() == search_song.lower()]
            print(tabulate(search_list ,headers=header, tablefmt="double_outline"))
        elif choose_menu == "0" :
            break
            
        os.system("pause")
            
if __name__ == "__main__" :
    main()