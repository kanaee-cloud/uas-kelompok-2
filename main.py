import os

def clear_screen():
    try:
        from google.colab import output # pyright: ignore[reportMissingImports]
        output.clear()
    except ImportError:
        os.system("cls")
        
def print_header(msg):
    print(f"{msg: ^50}")
    print(f"{'-'*50 : ^50}")
    
def pause():
    input("\nTekan enter untuk kembali ke menu utama...")

list_contact = [
    {
        "nik": "1234567890",
        "name": "John Doe",
        "phone": "555-1234",
        "email" : "john@example.com",
        "city" : "New York"

    },
    {
        "nik": "0987654321",
        "name": "Aane Smith",
        "phone": "555-5678",
        "email" : "aane@example.com",
        "city" : "Las Vegas"
    }
]

def create_contact():
    clear_screen()
    print_header("Menu Menambahkan Kontak (Pilihan 1)")
    nik = input("\nMasukkan NIK             : ")
    name = input("Masukkan nama kontak      : ").title()
    phone = input("Masukkan nomor kontak    : ")
    email = input("Masukkan email kontak    : ")
    city = input("Masukkan kota kontak      : ").title()
    contact = {
        "nik": nik,
        "name": name,
        "phone": phone,
        "email": email,
        "city": city
    }
    list_contact.append(contact)
    print("Kontak berhasil ditambahkan.")

    pause()

def contact_table():
    clear_screen()
    print_header("Menu Menampilkan Daftar Kontak (Pilihan 2)")

    print("\n")
    print("-" * 108)
    print(f"| {'No':<5} | {'NIK':<10} | {'Nama':<20} | {'Nomor':<15} | {'Email':<25} | {'Kota':<15}|")
    print("-" * 108)

    for idx, contact in enumerate(list_contact, start=1):
        print(f"| {idx:<5} | {contact['nik']:<10} | {contact['name']:<20} | {contact['phone']:<15} | {contact['email']:<25} | {contact['city']:<15}|")
        print("-" * 108)
    pause()

def search_contact():
    clear_screen()
    print_header("Menu Mencari Kontak (Pilihan 3)")
    nik = input("\nMasukkan NIK kontak yang ingin dicari: ")
    for contact in list_contact:
        if contact["nik"] == nik:
            print(f"\n{'NIK':<10} | {'Name':<20} | {'Phone':<15}")
            print("-" * 50)
            print(f"{contact['nik']:<10} | {contact['name']:<20} | {contact['phone']:<15}")
            print("-" * 50)

        else:
            print("Kontak tidak ditemukan.")

    pause()

def sort_contact():
    clear_screen()
    print_header("Menu Mengurutkan Daftar Kontak (Pilihan 6)")

    print("\nPilih metode pengurutan:")
    print("1. Urutkan dari A-Z")
    print("2. Urutkan dari Z-A")

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

def edit_contact():
    clear_screen()
    print_header("Menu Mengubah Kontak (Pilihan 4)")

    nik = input("\nMasukkan NIK kontak yang akan diubah: ")
    for contact in list_contact:
        if contact["nik"] == nik:
            new_nik = input("Masukkan NIK baru              : ")
            new_name = input("Masukkan nama baru            : ").title()
            new_phone = input("Masukkan nomor telepon baru  : ")
            new_email = input("Masukkan email baru          : ")
            new_city = input("Masukkan kota baru            : ").title()
            contact["nik"] = new_nik
            contact["name"] = new_name
            contact["phone"] = new_phone
            contact["email"] = new_email
            contact["city"] = new_city
            print("Kontak berhasil diperbarui.")
            return
        else:
            print("Kontak tidak ditemukan.")
    
    pause()

def delete_contact():
    clear_screen()
    print_header("Menu Menghapus Kontak (Pilihan 5)")
    nik = input("\nMasukkan NIK kontak yang akan dihapus: ")
    for contact in list_contact:
        if contact["nik"] == nik:
            list_contact.remove(contact)
            print("Kontak berhasil dihapus.")

        else:
            print("Kontak tidak ditemukan.")

    pause()


def menu():
    while True:
        clear_screen()

        print_header("Aplikasi Daftar Kontak Sederhana")

        print(f"\n{'Menu Utama': ^25}")
        print("1. Menambahkan Kontak")
        print("2. Menampilkan Daftar Kontak")
        print("3. Mencari Kontak")
        print("4. Mengubah Kontak")
        print("5. Menghapus Kontak")
        print("6. Mengurutkan Daftar Kontak")
        print("7. Keluar dari Menu")

        pilihan_menu = int(input("Masukkan pilihan Anda: "))


        if pilihan_menu == 1:
            create_contact()

        elif pilihan_menu == 2:
            contact_table()

        elif pilihan_menu == 3:
            search_contact()

        elif pilihan_menu == 4:
            edit_contact()

        elif pilihan_menu == 5:
            delete_contact()

        elif pilihan_menu == 6:
            sort_contact()

        elif pilihan_menu == 7:
            clear_screen()
            print("Keluar dari menu.")
            break

        else:
            print("Pilihan tidak valid.")


menu()