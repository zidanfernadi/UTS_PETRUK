BATAS_STOK_MENIPIS = 10

def hitung_total(*angka):
    return sum(angka)

def hitung_rata(*angka):
    assert len(angka) > 0, "Minimal harus ada satu angka"
    return sum(angka) / len(angka)

def format_rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")

class Barang:

    def __init__(self, kode, nama, harga, stok, **info):
        self.kode, self.nama, self.harga, self.stok = kode, nama, harga, stok
        self.info = info

    def hitung_nilai(self):
        return self.harga * self.stok

    def ke_baris(self):
        kategori = self.info.get("kategori", "-")
        return f"{self.kode};{self.nama};{self.harga};{self.stok};{kategori}"

class Inventaris:

    def __init__(self, daftar_barang=None):
        self.daftar_barang = daftar_barang or []

    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)

    def hitung_total_nilai(self):
        semua_nilai = map(lambda b: b.hitung_nilai(), self.daftar_barang)
        return hitung_total(*semua_nilai)

    def hitung_rata_harga(self):
        return hitung_rata(*[b.harga for b in self.daftar_barang])

    def urutkan_barang(self, berdasarkan="harga", terbalik=False):
        aturan = {"harga": lambda b: b.harga,
                  "stok": lambda b: b.stok,
                  "nama": lambda b: b.nama.lower()}
        return sorted(self.daftar_barang, key=aturan[berdasarkan], reverse=terbalik)

    def cari_stok_menipis(self, batas=BATAS_STOK_MENIPIS):
        return list(filter(lambda b: b.stok <= batas, self.daftar_barang))

    def buat_laporan(self, batas_stok=BATAS_STOK_MENIPIS):
        if not self.daftar_barang:
            return "Belum ada data barang."
        termahal = max(self.daftar_barang, key=lambda b: b.harga)
        menipis = self.cari_stok_menipis(batas=batas_stok)
        total = format_rupiah(self.hitung_total_nilai())
        rata = format_rupiah(self.hitung_rata_harga())
        baris = ["===== LAPORAN INVENTARIS TOKO =====",
                 f"Jumlah jenis barang : {len(self.daftar_barang)}",
                 f"Total nilai stok    : {total}",
                 f"Rata-rata harga     : {rata}",
                 f"Barang termahal     : {termahal.nama}",
                 f"Stok menipis        : {len(menipis)} barang (<= {batas_stok})"]
        baris += [f"  - {b.nama} (sisa {b.stok})" for b in menipis]
        return "\n".join(baris)