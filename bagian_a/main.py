from hitung import tampilkan_hasil

nilai_budi = [80, 75, 90]
nilai_sari = [60, 65, 55, 70]

tampilkan_hasil("Budi", *nilai_budi)
print()
tampilkan_hasil("Sari", *nilai_sari, batas_lulus=70)