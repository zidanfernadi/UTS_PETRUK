# test_suhu.py
# Pengujian fungsi analisis_suhu memakai unittest
import unittest
from suhu import analisis_suhu, hitung_rata_rata


class TestAnalisisSuhu(unittest.TestCase):

    def setUp(self):
        # data uji disiapkan baru sebelum tiap pengujian
        self.data = [
            {"hari": "Senin", "suhu": 31},
            {"hari": "Selasa", "suhu": 33},
            {"hari": "Rabu", "suhu": 29},
            {"hari": "Kamis", "suhu": 35},
            {"hari": "Jumat", "suhu": 32},
            {"hari": "Sabtu", "suhu": 30},
            {"hari": "Minggu", "suhu": 28},
        ]

    def test_rata_rata(self):
        hasil = analisis_suhu(self.data)
        self.assertAlmostEqual(hasil["rata_rata"], 31.14, places=2)

    def test_suhu_tertinggi(self):
        hasil = analisis_suhu(self.data)
        self.assertEqual(hasil["tertinggi"]["hari"], "Kamis")
        self.assertEqual(hasil["tertinggi"]["suhu"], 35)

    def test_suhu_terendah(self):
        hasil = analisis_suhu(self.data)
        self.assertEqual(hasil["terendah"]["hari"], "Minggu")

    def test_jumlah_hari_panas(self):
        # Selasa (33), Kamis (35), dan Jumat (32) -> 3 hari
        hasil = analisis_suhu(self.data)
        self.assertEqual(hasil["jumlah_panas"], 3)

    def test_batas_kategori(self):
        # suhu 32 sudah Panas, suhu 31 masih Normal
        hasil = analisis_suhu(self.data)
        kategori = {d["hari"]: d["kategori"] for d in hasil["data"]}
        self.assertEqual(kategori["Jumat"], "Panas")
        self.assertEqual(kategori["Senin"], "Normal")

    def test_args_rata_rata(self):
        self.assertEqual(hitung_rata_rata(30, 32, 34), 32)


if __name__ == "__main__":
    unittest.main()
