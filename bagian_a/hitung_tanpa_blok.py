BATAS_LULUS = 70


def hitung_rata_rata(*nilai):
    total = 0
    for n in nilai:
        total += n
    return total / len(nilai)

print("Uji rata-rata (80, 75, 90) =", hitung_rata_rata(80, 75, 90))
