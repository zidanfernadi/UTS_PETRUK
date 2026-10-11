# baca_nilai_perbaikan.py : versi yang sudah diperbaiki
def baca_data(nama_file):
    data = []
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                try:
                    npm, nama, nilai = baris.strip().split(";")
                    nilai = int(nilai)
                    data.append({"npm": npm, "nama": nama, "nilai": nilai})
                except ValueError:
                    print("Baris dilewati (tidak valid):", baris.strip())
    except FileNotFoundError:
        print("File tidak ditemukan")
    return data
hasil = baca_data("nilai.txt")
print(hasil)