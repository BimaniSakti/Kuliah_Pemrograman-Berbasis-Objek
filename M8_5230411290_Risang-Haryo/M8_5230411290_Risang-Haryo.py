from tkinter import ttk, messagebox, filedialog
import tkinter as tk
import pandas as pd
import datetime as dt


class StuffStock:
    def __init__(self, window):
        '''Untuk menginisialisasi beberapa hal yang dibutuhkan secara langsung'''
        self.window = window
        self.window.title("Aplikasi Penyimpanan Stok Barang")
        self.window.geometry("700x600")
        self.window.configure(bg="#242158")
        self.cateogry_dict = {"Furnitur":"Sekat A", "Elektronik":"Sekat B", "Perkakas":"Sekat C", "Bahan Material":"Sekat D", "Lainnya":"Sekat E"}
        self.unit_list = ["Kilogram", "Meter", "Liter", "Unit", "Kardus", "Sak"]
        
    def createWidget(self):
        def initVars() -> None:
            '''Fungsi untuk menginisalisasi semua variabel yang digunakan untuk menampung inputan user secara real time di entry form'''
            self.name_var = tk.StringVar()
            self.category_var = tk.StringVar()
            self.qty_var = tk.StringVar()
            self.unit_var = tk.StringVar()
            self.location_var = tk.StringVar()
            self.category_var.trace_add("write", generateLocate)
            self.qty_var.trace_add("write", validateData)
        
        def isfloat(value) -> None:
            '''Fungsi untuk memvalidasi input pengguna harus bertipe data float'''
            try:
                float(value)
                return True
            except ValueError:
                return False
            
        def resetForm() -> None:
            '''Fungsi untuk mengosongkan formulir'''
            for var in (self.name_var, self.category_var, self.qty_var, self.unit_var, self.location_var):
                var.set('')    
            
        def validateData(*args) -> None:
            '''Fungsi untuk memberikan penanda jika jumlah tidak berupa angka'''
            self.qty_entry.config(bg='white' if (isfloat(self.qty_var.get()) or self.qty_var.get() == "") else 'pink')
                
        def generateLocate(*args) -> None:
            '''Fungsi untuk mendapatkan value dari Lokasi berdasarkan kategori barang'''
            category = self.category_var.get()
            if category and category in self.cateogry_dict:
                location = self.cateogry_dict[category]
                self.location_var.set(f"{location}")
        
        def addData():
            '''Fungsi untuk menambahkan barang ke gudang'''
            name = self.name_var.get()
            category = self.category_var.get()
            qty = self.qty_var.get()
            unit = self.unit_var.get()
            
            # Untuk memeriksa apakah ada nama yang sama lalu memberikan pesan tertentu
            for item in self.stuff_table.get_children():
                item_values = self.stuff_table.item(item, 'values')
                if item_values[0].lower() == name.lower():
                    messagebox.showwarning("", f"{name} Sudah Ada")
                    return
            
            # Untuk memeriksa apakah semua form sudah terisi
            if name and category and isfloat(qty) and unit:
                float(qty)
                location = self.cateogry_dict[category]
                datetime = dt.date.today()
                self.stuff_table.insert("", "end", values=(name, category, qty, unit, location, datetime))
                resetForm() # Untuk mengosongkan form
            else:
                messagebox.showerror("Error", "Pastikan Formulir Terisi Semua dan Jumlah Barang Berupa Angka")
                
        def deleteData():
            '''Fungsi untuk menghapus barang atau beberapa barang yang dipilih'''
            selected_item = self.stuff_table.selection()
            if not selected_item:
                messagebox.showerror("Error", "Tidak ada barang yang dipilih")
                return
            
            # Untuk konfirmasi apakah yakin ingin menghapus barang ini?
            confirm = messagebox.askyesno("Konfirmasi", "Yakin Ingin Menghapus Barang Ini?")
            if confirm == False:
                return
            for item in selected_item:
                self.stuff_table.delete(item)
            messagebox.showinfo("Info", "Barang Berhasil Dihapus")
            
        def editData():
            '''Fungsi untuk memilih data yang hendak diedit 
            (disarankan untuk memilih salah satu barang saja karena jika memillih lebih dari satu,
            maka yang akan diambil adalah barang yang dipilih pertama kali)'''
            selected_item = self.stuff_table.selection()
            if not selected_item:
                messagebox.showerror("Error", "Tidak ada barang yang dipilih")
                return
            
            # Memastikan yang dibisa diedit adalah barang yang pertama kali dipilih
            item_values = self.stuff_table.item(selected_item[0], option='values')
            variables = [self.name_var, self.category_var, self.qty_var, self.unit_var, self.location_var]
            for i, var in enumerate(variables):
                var.set(item_values[i])
            self.id_selected_item = selected_item[0]
            
        def updateData():
            '''Untuk memperbaharui barang yang telah dipilih'''
            # menyingkronkan barang yang dipilih sesuai dengan fungsi editData
            if not hasattr(self, 'id_selected_item') or not self.id_selected_item:
                messagebox.showerror("", "Tidak Ada Data Yang Harus Diupdate")
                return
            
            # Sama seperti fungsi addData tetapi mengganti value barang yang dipilih
            name = self.name_var.get()
            category = self.category_var.get()
            qty = self.qty_var.get()
            unit = self.unit_var.get()
            
            # Untuk memeriksa apakah ada nama yang sama lalu memberikan pesan tertentu
            for item in self.stuff_table.get_children():
                item_values = self.stuff_table.item(item, 'values')
                if item_values[0].lower() == name.lower():
                    messagebox.showwarning("", f"{name} Sudah Ada")
                    return
            
            if name and category and isfloat(qty) and unit:
                float(qty)
                location = self.cateogry_dict[category]
                datetime = dt.date.today()
                self.stuff_table.item(self.id_selected_item, values=(name, category, qty, unit, location, datetime))
                self.id_selected_item = None
                resetForm()
                messagebox.showinfo("", "Berhasil mengubah barang")
            else:
                messagebox.showerror("Error", "Pastikan Formulir Terisi Semua dan Jumlah Barang Berupa Angka")
                
        def exportFile():
            '''Untuk mengekspor file ke bentuk spreadsheet'''
            # Menambahkan semua item di tabel ke tipe data list
            data = []
            for value in self.stuff_table.get_children():
                values = self.stuff_table.item(value, 'values')
                data.append(values)
            
            # Memeriksa jika data kosong maka memunculkan pesan tertentu
            if data == []:
                messagebox.showerror("", "Tidak Ada Data Yang Diekspor")
                return
            
            df = pd.DataFrame(data, columns=("Nama", "Kategori", "Jumlah", "Satuan", "Lokasi", "Tanggal"))
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Excel", "*.xlsx"), ("CSV", "*.csv")], title="Simpan File")
            
            if file_path:
                if file_path.endswith(".csv"):
                    df.to_csv(file_path, index=False)
                else:
                    df.to_excel(file_path, index=False)
                messagebox.showinfo("Sukses", f"Data berhasil diekspor ke {file_path}!")
                
        def importFile():
            '''Untuk mengimpor file Excel atau CSV'''
            file_path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv"), ("Excel", "*.xlsx")] , title="Cari File")
            
            if file_path:
                if file_path.endswith(".csv"):
                    df = pd.read_csv(file_path)
                else:
                    df = pd.read_excel(file_path)
            else:
                return
                
            for item in self.stuff_table.get_children():
                self.stuff_table.delete(item)
            
            for i, value in df.iterrows():
                self.stuff_table.insert("", "end", values=tuple(value))
            
            messagebox.showinfo("Sukses", f"Data berhasil diimpor")
            
        ## Mengganti Tema
        style = ttk.Style().theme_use('clam')
            
        ## Mengonfigurasi Grid 
        self.window.grid_columnconfigure(0, weight=1) 
        self.window.grid_rowconfigure(3, weight=1)
        
        ## Label Judul
        title_label = tk.Label(self.window, text="Selamat Datang di Gudang", bg="#242158", font=("Helvetica", 16, "bold"), foreground="white")
        title_label.grid(row=0, column=0, pady=8)
        
        ## Membuat Frame Bagian Atas
        top_frame = tk.Frame(self.window, bg="#213a58", relief="solid", borderwidth=1)
        top_frame.grid(row=1, column=0, sticky="nesw", padx=10, pady=10)
        top_frame.columnconfigure(0, weight=1)
        top_frame.columnconfigure(1, weight=3)
        
        # Menginisialisasi semua var
        initVars()
        
        # Nama Barang
        name_label = tk.Label(top_frame, text="Nama Barang : ", bg="#213a58", font=("Helvetica", 10, "bold"), foreground="white")
        name_label.grid(row=0, column=0, sticky="w", padx=4, pady=4)
        self.name_entry = tk.Entry(top_frame, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=4, pady=4)
        
        # Kategori Barang
        category_label = tk.Label(top_frame, text="Kategori Barang : ", bg="#213a58", font=("Helvetica", 10, "bold"), foreground="white")
        category_label.grid(row=1, column=0, sticky="w", padx=4, pady=4)
        self.category_option = ttk.Combobox(top_frame, textvariable=self.category_var, values=list(self.cateogry_dict.keys()), state="readonly")
        self.category_option.grid(row=1, column=1, sticky="ew", padx=4, pady=4)
        
        # Jumlah Barang
        qty_label = tk.Label(top_frame, text="Jumlah Barang : ", bg="#213a58", font=("Helvetica", 10, "bold"), foreground="white")
        qty_label.grid(row=2, column=0, sticky="w", padx=4, pady=4)
        self.qty_entry = tk.Entry(top_frame, textvariable=self.qty_var)
        self.qty_entry.grid(row=2, column=1, sticky="ew", padx=4, pady=4)
        
        # Satuan Barang
        unit_label = tk.Label(top_frame, text="Satuan Barang : ", bg="#213a58", font=("Helvetica", 10, "bold"), foreground="white")
        unit_label.grid(row=3, column=0, sticky="w", padx=4, pady=4)
        self.unit_option = ttk.Combobox(top_frame, textvariable=self.unit_var, values=self.unit_list, state="readonly")
        self.unit_option.grid(row=3, column=1, sticky="ew", padx=4, pady=4)
        
        # Lokasi Penempatan Barang
        location_label = tk.Label(top_frame, text="Lokasi Penempatan : ", bg="#213a58", font=("Helvetica", 10, "bold"), foreground="white")
        location_label.grid(row=4, column=0, sticky="w", padx=4, pady=4)
        self.location_entry = tk.Entry(top_frame, textvariable=self.location_var, state="readonly")
        self.location_entry.grid(row=4, column=1, sticky="ew", padx=4, pady=4)
        
        ## Membuat Frame Bagian Tengah
        middle_frame = tk.Frame(self.window, bg="#242158")
        middle_frame.grid(row=2, column=0, sticky="nesw", padx=10)
        
        # Tombol Taruh Gudang
        self.submit_btn = ttk.Button(middle_frame, text="Taruh", command=addData)
        self.submit_btn.pack(side='right')
        
        # Tombol Update Barang yang DIpilih
        self.update_btn = ttk.Button(middle_frame, text="Update", command=updateData)
        self.update_btn.pack(side='right', padx=4)
        
        # Tombol Edit Barang yang Dipilih
        self.edit_btn = ttk.Button(middle_frame, text="Edit", command=editData)
        self.edit_btn.pack(side='right')
        
        # Tombol Hapus barang yang dipilih
        self.delete_btn = ttk.Button(middle_frame, text="Hapus", command=deleteData)
        self.delete_btn.pack(side='right', padx=4)
        
        # Tombol Export ke Spreadsheet
        self.export_btn = ttk.Button(middle_frame, text="Ekspor File", command=exportFile)
        self.export_btn.pack(side='left')
        
        # Tombol Import ke Python
        self.import_btn = ttk.Button(middle_frame, text="Impor File", command=importFile)
        self.import_btn.pack(side='left', padx=4)
        
        ## Membuat Frame Bagian Bawah
        bottom_frame = tk.Frame(self.window, bg="#213a58", relief="solid", borderwidth=1)
        bottom_frame.grid(row=3, column=0, sticky="nesw", padx=10, pady=10)
        
        # Label Tabel
        title_label = tk.Label(bottom_frame, text="Daftar Barang", bg="#213a58", font=("Helvetica", 12, "bold"), foreground="white")
        title_label.pack(fill="both")
        
        # Daftar Barang Heading
        self.stuff_table = ttk.Treeview(bottom_frame, columns=("Nama", "Kategori", "Jumlah", "Satuan", "Lokasi", "Tanggal"), show="headings")
        self.stuff_table.heading("Nama", text="Nama")
        self.stuff_table.heading("Kategori", text="Kategori")
        self.stuff_table.heading("Jumlah", text="Jumlah")
        self.stuff_table.heading("Satuan", text="Satuan")
        self.stuff_table.heading("Lokasi", text="Lokasi")
        self.stuff_table.heading("Tanggal", text="Tanggal")
        
        # Daftar Barang Body
        self.stuff_table.column("Nama", anchor="w", width=150)
        self.stuff_table.column("Kategori", anchor="w", width=50)
        self.stuff_table.column("Jumlah", anchor="e", width=10)
        self.stuff_table.column("Satuan", anchor="w", width=10)
        self.stuff_table.column("Lokasi", anchor="w", width=50)
        self.stuff_table.column("Tanggal", anchor="w", width=50)
        self.stuff_table.pack(fill="both", expand=True, padx=12, pady=12)


if __name__ == "__main__":
    window = tk.Tk()
    stock = StuffStock(window)
    stock.createWidget()
    window.mainloop()