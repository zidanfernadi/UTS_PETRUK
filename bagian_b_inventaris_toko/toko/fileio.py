from .processing import Barang
from .validasi import parse_baris, DataTidakValidError

NAMA_FILE_DATA = "data_barang.txt"
NAMA_FILE_LAPORAN = "laporan_inventaris.txt"

DATA_AWAL = ["B001;Beras 5kg;65000;25;Sembako",
             "B002;Minyak Goreng 1L;18000;8;Sembako",
             "B003;Gula Pasir 1kg;16000;30;Sembako",
             "B004;Mie Instan;3500;120;Makanan",
             "B005;Teh Botol;5000;6;Minuman",
             "B006;Kopi Sachet;1500;200;Minuman",
             "B007;Sabun Mandi;4500;15;Kebersihan",
             "B008;Deterjen 800g;22000;4;Kebersihan"]

def pesan_file_belum_ada(nama_file):
    print(f"Error: file {nama_file} belum ada, buat dulu lewat menu 1.")

def buat_file(nama_file):
    try:
        with open(nama_file, "x") as file:
            file.write("\n".join(DATA_AWAL) + "\n")
        print(f"File {nama_file} berhasil dibuat dengan {len(DATA_AWAL)} data awal.")
    except FileExistsError:
        print(f"Gagal: file {nama_file} sudah ada, data lama tidak ditimpa.")

def tambah_data(nama_file, barang):
    try:
        with open(nama_file, "r"):
            pass
    except FileNotFoundError:
        return pesan_file_belum_ada(nama_file)
    with open(nama_file, "a") as file:
        file.write(barang.ke_baris() + "\n")
    print(f"Barang '{barang.nama}' berhasil ditambahkan.")

def baca_data(nama_file):
    daftar_barang, jumlah_rusak = [], 0
    try:
        with open(nama_file, "r") as file:
            for nomor, baris in enumerate(file, start=1):
                if baris.strip() == "":
                    continue 
                try:
                    daftar_barang.append(Barang(**parse_baris(baris)))
                except (ValueError, DataTidakValidError) as e:
                    print(f"[PERINGATAN] Baris {nomor} dilewati: {e}")
                    jumlah_rusak += 1
    except FileNotFoundError:
        pesan_file_belum_ada(nama_file)
    return daftar_barang, jumlah_rusak

def tulis_laporan(nama_file, isi_laporan):
    with open(nama_file, "w") as file:
        file.write(isi_laporan + "\n")
    print(f"Laporan berhasil ditulis ke {nama_file}")

def tampilkan_isi_file(nama_file):
    try:
        with open(nama_file, "r") as file:
            print(file.read().rstrip())
    except FileNotFoundError:
        pesan_file_belum_ada(nama_file)