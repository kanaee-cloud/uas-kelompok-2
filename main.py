import os

def clear_screen():
    try:
        from google.colab import output
        output.clear()
    except ImportError:
        os.system("cls")

list_contact = [
    {
        "nik": "1234567890", 
        "name": "John Doe",
        "phone": "555-1234"
        
    },
    {
        "nik": "0987654321", 
        "name": "Aane Smith",
        "phone": "555-5678"
    }
]

def create_contact():
    clear_screen()
    print(f"{'Menu Menambahkan Kontak (Pilihan 1)': ^50}")
    print(f"{'-'*50 : ^50}")
    nik = input("\nMasukkan NIK: ")
    name = input("Masukkan nama kontak: ").title()
    phone = input("Masukkan nomor kontak: ")
    contact = {
        "nik": nik, 
        "name": name, 
        "phone": phone
    }
    list_contact.append(contact)
    print("Kontak berhasil ditambahkan.")

    input("\nTekan enter untuk kembali ke menu utama...")
    
def contact_table():
    clear_screen()
    print(f"{'Menu Menampilkan Daftar Kontak (Pilihan 2)': ^50}")
    print(f"{'-'*50 : ^50}")

    print(f"\n{'NIK':<10} | {'Name':<20} | {'Phone':<15}")
    print("-" * 50)
    
    for contact in list_contact:
        print(f"{contact['nik']:<10} | {contact['name']:<20} | {contact['phone']:<15}")
        print("-" * 50)
        
    input("\nTekan enter untuk kembali ke menu utama...")

def edit_contact():
    clear_screen()
    print(f"{'Menu Mengubah Kontak (Pilihan 4)': ^50}")
    print(f"{'-'*50 : ^50}")

    nik = input("\nMasukkan NIK kontak yang akan diubah: ")
    for contact in list_contact:
        if contact["nik"] == nik:
            new_nik = input("Masukkan NIK baru: ")
            new_name = input("Masukkan nama baru: ")
            new_phone = input("Masukkan nomor telepon baru: ")
            contact["nik"] = new_nik
            contact["name"] = new_name
            contact["phone"] = new_phone
            print("Kontak berhasil diperbarui.")
            return
    print("Kontak tidak ditemukan.")

    input("\nTekan enter untuk kembali ke menu utama...")
    
# def menu():
#     print("test")

# def main():
#     while True:
#         print(f"{'PROGRAM MANAJEMEN KONTAK': ^50}")
#         print(f"{'-'*50 : ^50}")


def menu():
    while True:
        clear_screen()

        print(f"{'PROGRAM MANAJEMEN KONTAK': ^50}")
        print(f"{'-'*50 : ^50}")
    
        print(f"""\n{'Menu Utama': ^25}
\n1. Menambahkan Kontak
2. Menampilkan Daftar Kontak
3. Mencari Kontak
4. Mengubah Kontak
5. Menghapus Kontak
6. Mengurutkan Daftar Kontak
7. Keluar
""")

        pilihan_menu = int(input("Masukkan pilihan Anda: "))

    
        if pilihan_menu == 1:
            create_contact()
        
        elif pilihan_menu == 2:
            contact_table()

        elif pilihan_menu == 3:
            pass

        elif pilihan_menu == 4:
            edit_contact()

        elif pilihan_menu == 5:
            pass

        elif pilihan_menu == 6:
            sort_contact()

        elif pilihan_menu == 7:
            clear_screen()
            print("Keluar dari menu.")
            break

        else:
            print("Pilihan tidak valid.")
            
def sort_contact():
    clear_screen()
    print(f"{'Menu Mengurutkan Daftar Kontak (Pilihan 6)': ^50}")
    print(f"{'-'*50 : ^50}")

    print("""\n1. Berdasarkan Nama (A-Z)
2. Berdasarkan Nama (Z-A)
""")
    
    sort_pilih = int(input("\nMasukkan pilihan Anda: "))
    
    if sort_pilih == 1:
        list_contact.sort(key=lambda x: x["name"].title())
        print(".")

        contact_table()

    elif sort_pilih == 2:
        list_contact.sort(key=lambda x: x["name"].title(), reverse=True)

        contact_table()


    else:
        print("Pilihan tidak valid.")
    
#     menu()
#     create_contact()
#     # edit_contact()
#     contact_table()
    
# main()

menu()





