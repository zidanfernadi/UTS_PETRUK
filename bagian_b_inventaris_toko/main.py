import toko

DATA = toko.NAMA_FILE_DATA
LAPORAN = toko.NAMA_FILE_LAPORAN

MENU = """
===== PROGRAM INVENTARIS TOKO =====
1. Buat file data baru
2. Tambah barang
3. Tampilkan semua barang
4. Urutkan barang
5. Cek stok menipis
6. Buat laporan inventaris
0. Keluar"""


def cetak_tabel(daftar_barang):
    print(f"{'Kode':<6}{'Nama':<20}{'Harga':>12}{'Stok':>7}  {'Kategori'}")
    print("-" * 58)
    for b in daftar_barang:
        kategori = b.info.get("kategori", "-")
        harga = toko.format_rupiah(b.harga)
        print(f"{b.kode:<6}{b.nama:<20}{harga:>12}{b.stok:>7}  {kategori}")


def ambil_inventaris():
    daftar_barang, rusak = toko.baca_data(DATA)
    return toko.Inventaris(daftar_barang) if daftar_barang else None


def menu_tambah():
    print("\n--- Tambah Barang ---")
    try:
        kode = toko.cek_tidak_kosong(input("Kode barang : "), "Kode")
        nama = toko.cek_tidak_kosong(input("Nama barang : "), "Nama")
        harga = toko.cek_angka_positif(input("Harga       : "), "Harga")
        stok = toko.cek_angka_positif(input("Stok        : "), "Stok")
        kategori = toko.cek_tidak_kosong(input("Kategori    : "), "Kategori")
    except ValueError: 
        return print("Input gagal: harga dan stok harus berupa angka bulat!")
    except toko.DataTidakValidError as e:
        return print("Input gagal:", e)
    toko.tambah_data(DATA, toko.Barang(kode, nama, harga, stok, kategori=kategori))


def menu_tampilkan():
    inv = ambil_inventaris()
    if inv:
        print("\n--- Daftar Barang ---")
        cetak_tabel(inv.daftar_barang)


def menu_urutkan():
    inv = ambil_inventaris()
    if not inv:
        return
    pilihan = {"1": "harga", "2": "stok", "3": "nama"}
    print("\nUrutkan berdasarkan: 1. Harga  2. Stok  3. Nama")
    kunci = input("Pilih (1-3): ")
    if kunci not in pilihan:
        return print("Pilihan tidak valid!")
    terbalik = input("Dari yang terbesar/Z ke A? (y/n): ").lower() == "y"
    print(f"\n--- Barang diurutkan berdasarkan {pilihan[kunci]} ---")
    cetak_tabel(inv.urutkan_barang(berdasarkan=pilihan[kunci], terbalik=terbalik))


def menu_menipis():
    inv = ambil_inventaris()
    if inv:
        print(f"\n--- Barang dengan stok <= {toko.BATAS_STOK_MENIPIS} ---")
        cetak_tabel(inv.cari_stok_menipis(batas=toko.BATAS_STOK_MENIPIS))


def menu_laporan():
    inv = ambil_inventaris()
    if inv:
        isi = inv.buat_laporan(batas_stok=toko.BATAS_STOK_MENIPIS)
        toko.tulis_laporan(LAPORAN, isi)
        print("\nIsi laporan:")
        toko.tampilkan_isi_file(LAPORAN)


def main():
    aksi = {"1": lambda: toko.buat_file(DATA), "2": menu_tambah,
            "3": menu_tampilkan, "4": menu_urutkan,
            "5": menu_menipis, "6": menu_laporan}
    while True: 
        print(MENU)
        pilihan = input("Pilih menu: ")
        if pilihan == "0":
            print("Terima kasih, program selesai.")
            break
        aksi.get(pilihan, lambda: print("Menu tidak tersedia, coba lagi."))()


if __name__ == "__main__":
    main()