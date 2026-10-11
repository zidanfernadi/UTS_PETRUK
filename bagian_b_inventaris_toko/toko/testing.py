import os
import unittest

from .validasi import (cek_tidak_kosong, cek_angka_positif,
                       parse_baris, DataTidakValidError)
from .processing import Barang, Inventaris, hitung_total, hitung_rata
from .fileio import buat_file, tambah_data, baca_data


class TestValidasi(unittest.TestCase):

    def test_field_kosong(self):
        with self.assertRaises(DataTidakValidError):
            cek_tidak_kosong("   ", "Nama")

    def test_angka_negatif(self):
        with self.assertRaises(DataTidakValidError):
            cek_angka_positif("-10", "Stok")

    def test_bukan_angka(self):
        with self.assertRaises(ValueError):
            cek_angka_positif("abc", "Harga")

    def test_parse_baris_benar(self):
        hasil = parse_baris("B001;Beras 5kg;65000;25;Sembako")
        self.assertEqual(hasil["harga"], 65000)

    def test_parse_baris_kolom_kurang(self):
        with self.assertRaises(DataTidakValidError):
            parse_baris("B001;Beras 5kg;65000")


class TestProcessing(unittest.TestCase):

    def setUp(self):
        self.inv = Inventaris()
        self.inv.tambah_barang(Barang("A1", "Beras", 60000, 10, kategori="Sembako"))
        self.inv.tambah_barang(Barang("A2", "Gula", 16000, 5, kategori="Sembako"))
        self.inv.tambah_barang(Barang("A3", "Kopi", 2000, 100, kategori="Minuman"))

    def test_args(self):
        self.assertEqual(hitung_total(10, 20, 30), 60)
        self.assertEqual(hitung_rata(80, 70, 90), 80)

    def test_assert_data_kosong(self):
        with self.assertRaises(AssertionError):
            hitung_rata()

    def test_kwargs_dan_nilai_barang(self):
        barang = Barang("X1", "Teh", 5000, 4, kategori="Minuman", supplier="CV Maju")
        self.assertEqual(barang.hitung_nilai(), 20000)
        self.assertEqual(barang.info["supplier"], "CV Maju")

    def test_total_nilai(self):
        self.assertEqual(self.inv.hitung_total_nilai(), 880000)

    def test_urutkan_harga(self):
        hasil = self.inv.urutkan_barang(berdasarkan="harga", terbalik=True)
        self.assertEqual(hasil[0].nama, "Beras")

    def test_stok_menipis(self):
        nama = [b.nama for b in self.inv.cari_stok_menipis(batas=10)]
        self.assertEqual(nama, ["Beras", "Gula"])


class TestFileIO(unittest.TestCase):
    NAMA = "data_uji_sementara.txt"

    def setUp(self):
        self.tearDown()
        buat_file(self.NAMA)

    def tearDown(self):
        if os.path.exists(self.NAMA):
            os.remove(self.NAMA)

    def test_buat_dan_baca(self):
        daftar, rusak = baca_data(self.NAMA)
        self.assertEqual((len(daftar), rusak), (8, 0))

    def test_baris_rusak_dilewati(self):
        with open(self.NAMA, "a") as file:
            file.write("B099;Rusak;abc;5;Lain\nB098;Negatif;1000;-3;Lain\n")
        daftar, rusak = baca_data(self.NAMA)
        self.assertEqual((len(daftar), rusak), (8, 2))

    def test_tambah_data(self):
        tambah_data(self.NAMA, Barang("B009", "Susu", 12000, 20, kategori="Minuman"))
        self.assertEqual(baca_data(self.NAMA)[0][-1].nama, "Susu")

    def test_file_tidak_ada(self):
        self.assertEqual(baca_data("file_tidak_ada.txt")[0], [])


if __name__ == "__main__":
    unittest.main()