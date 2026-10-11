class DataTidakValidError(Exception):
    pass 


def cek_tidak_kosong(teks, nama_field):
    teks = teks.strip()
    if teks == "" or ";" in teks:
        raise DataTidakValidError(f"{nama_field} kosong atau mengandung ';'!")
    return teks


def cek_angka_positif(teks, nama_field):
    angka = int(teks)
    if angka < 0:
        raise DataTidakValidError(f"{nama_field} tidak boleh negatif!")
    return angka


def parse_baris(baris):
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
    print("Angka valid     :", cek_angka_positif("15", "Harga"))
    for isi in ("-5", "abc"):
        try:
            cek_angka_positif(isi, "Stok")
        except (DataTidakValidError, ValueError) as e:
            print(f"Input '{isi}'      -> {type(e).__name__}: {e}")
    print("parse_baris     :", parse_baris("B001;Beras 5kg;65000;25;Sembako"))
