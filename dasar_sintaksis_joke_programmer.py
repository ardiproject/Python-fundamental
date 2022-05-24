"""
Ini adalah demo project pertama dengan Python
Semua sintaksis bahasa pemrograman terdiri dari :
1. Sekuensial  : Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan  : Mengulangi langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
print("Helo World!")
print("My Name Is Ardi")
# sekuensial
print('ibu berkata,"tolong belikan susu satu botol"')
print('ardi menjawab,"baik bu"')
print('ibu berkata,"jangan lupa uangnya minta sama ayah"')
print("siap bosque!")

# Percabangan
jumlah_botol_susu = 15
jumlah_telur = 100
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("ardi mengecek harga,dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("ardi membeli 1 botol susu")
    else:
        print("ardi membeli 6 botol susu")
else:
    print("ardi tidak membeli 1 botol susu")

    print("ardi pulang kerumah")
    print("ardi menyampaikan hasil pada ibu")