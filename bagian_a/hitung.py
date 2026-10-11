BATAS_LULUS = 70

def hitung_rata_rata(*nilai):
    total = 0
    for n in nilai:
        total += n
    return total / len(nilai)

def tentukan_status(rata_rata, batas_lulus=BATAS_LULUS):
    return "Lulus" if rata_rata >= batas_lulus else "Tidak Lulus"

def tampilkan_hasil(nama, *nilai, batas_lulus=BATAS_LULUS):
    rata_rata = hitung_rata_rata(*nilai)
    print("Nama :", nama)
    print(f"Rata-rata :", f"{rata_rata:.2f}")
    print("Status :", tentukan_status(rata_rata, batas_lulus))

if __name__ == "__main__":
    print("Uji rata-rata (80, 75, 90) =", hitung_rata_rata(80, 75, 90))
    tampilkan_hasil("Uji", 60, 65, 55, 70)