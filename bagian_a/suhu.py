BATAS_PANAS = 32


def baca_suhu(nama_file):
    data = []
    try:
        with open(nama_file, "r") as file:
            for baris in file:
                if baris.strip() == "":
                    continue
                hari, suhu = baris.strip().split(";")
                data.append({"hari": hari, "suhu": int(suhu)})  # suhu bertipe angka
    except FileNotFoundError:
        print(f"Kesalahan: file {nama_file} tidak ditemukan!")
    return data


def hitung_rata_rata(*suhu):
    return sum(suhu) / len(suhu)


def analisis_suhu(data, batas_panas=BATAS_PANAS):
    semua_suhu = [d["suhu"] for d in data]
    rata_rata = hitung_rata_rata(*semua_suhu)

    tertinggi = max(data, key=lambda d: d["suhu"])
    terendah = min(data, key=lambda d: d["suhu"])

    kategori = lambda s: "Panas" if s >= batas_panas else "Normal"
    for d in data:
        d["kategori"] = kategori(d["suhu"])

    jumlah_panas = len(list(filter(lambda d: d["kategori"] == "Panas", data)))

    return {
        "rata_rata": rata_rata,
        "tertinggi": tertinggi,
        "terendah": terendah,
        "jumlah_panas": jumlah_panas,
        "data": data,
    }


def tulis_laporan(hasil, nama_file="laporan_suhu.txt"):
    with open(nama_file, "w") as file:
        file.write("===== LAPORAN SUHU MINGGUAN =====\n")
        for d in hasil["data"]:
            file.write(f"{d['hari']:<8}: {d['suhu']} C ({d['kategori']})\n")
        file.write("---------------------------------\n")
        file.write(f"Rata-rata suhu : {hasil['rata_rata']:.2f} C\n")
        tinggi = hasil["tertinggi"]
        rendah = hasil["terendah"]
        file.write(f"Suhu tertinggi : {tinggi['suhu']} C ({tinggi['hari']})\n")
        file.write(f"Suhu terendah  : {rendah['suhu']} C ({rendah['hari']})\n")
        file.write(f"Jumlah hari Panas : {hasil['jumlah_panas']} hari\n")


def tampilkan_laporan(nama_file="laporan_suhu.txt"):
    with open(nama_file, "r") as file:
        for baris in file:
            print(baris.rstrip())


def main():
    data = baca_suhu("suhu.txt")
    if len(data) == 0:
        return
    hasil = analisis_suhu(data, batas_panas=BATAS_PANAS)
    tulis_laporan(hasil, nama_file="laporan_suhu.txt")
    tampilkan_laporan(nama_file="laporan_suhu.txt")


if __name__ == "__main__":
    main()
