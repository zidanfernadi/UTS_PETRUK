# validasi.py
# Modul ini isinya fungsi-fungsi untuk mengecek input dan data
# sebelum data diproses atau disimpan ke file.
class DataTidakValidError(Exception):
    # Exception buatan sendiri, dipakai kalau data kosong atau negatif
    pass 


def cek_tidak_kosong(teks, nama_field):
    # Menghapus spasi di awal/akhir, lalu cek apakah field masih kosong.
    # Tanda ; juga dilarang karena dipakai sebagai pemisah kolom di file.
    teks = teks.strip()
    if teks == "" or ";" in teks:
        raise DataTidakValidError(f"{nama_field} kosong atau mengandung ';'!")
    return teks


def cek_angka_positif(teks, nama_field):
    # Menghapus spasi di awal/akhir, lalu cek apakah field masih kosong.
    # Tanda ; juga dilarang karena dipakai sebagai pemisah kolom di file.
    angka = int(teks)
    if angka < 0:
        raise DataTidakValidError(f"{nama_field} tidak boleh negatif!")
    return angka


def parse_baris(baris):
    # Menghapus spasi di awal/akhir, lalu cek apakah field masih kosong.
    # Tanda ; juga dilarang karena dipakai sebagai pemisah kolom di file.
    bagian = baris.strip().split(";")
    if len(bagian) != 5:
        raise DataTidakValidError("jumlah kolom harus 5")
    kode, nama, harga, stok, kategori = bagian
    return {"kode": cek_tidak_kosong(kode, "Kode"),
            "nama": cek_tidak_kosong(nama, "Nama"),
            "harga": cek_angka_positif(harga, "Harga"),
            "stok": cek_angka_positif(stok, "Stok"),
            "kategori": cek_tidak_kosong(kategori, "Kategori")}


if __name__ == "__main__":
    # Pengujian lokal, hanya jalan kalau file ini dieksekusi langsung
    print("Angka valid     :", cek_angka_positif("15", "Harga"))
    for isi in ("-5", "abc"):
        try:
            cek_angka_positif(isi, "Stok")
        except (DataTidakValidError, ValueError) as e:
            print(f"Input '{isi}'      -> {type(e).__name__}: {e}")
    print("parse_baris     :", parse_baris("B001;Beras 5kg;65000;25;Sembako"))
