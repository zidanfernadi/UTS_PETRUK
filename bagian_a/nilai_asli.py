nilai_budi = ["80", "75", "90"]
total = 0
for n in nilai_budi:
    total = total + n
rata = total / len(nilai_budi)
print("Nama : Budi")
print("Rata-rata :", rata)
if rata >= 70:
    print("Status : Lulus")
else:
    print("Status : Tidak Lulus")
