# baca_nilai_asli.py : program dari soal (belum diperbaiki)
def baca_data(nama_file):
    data = []
    with open(nama_file, "r") as file:
        for baris in file:
            npm, nama, nilai = baris.strip().split(";")
            data.append({"npm": npm, "nama": nama, "nilai": int(nilai)})
    return data


hasil = baca_data("nilai.txt")
print(hasil)


