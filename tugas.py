def hitung_biaya_parkir(jenis_kendaraan, lama_parkir):

    if jenis_kendaraan == "Mobil":
        tarif = 5000
    elif jenis_kendaraan == "Motor":
        tarif = 3000
    else:
        return 0

    total_biaya = tarif * lama_parkir
    return total_biaya


# Input data
jenis = input("Masukkan jenis kendaraan (Mobil/Motor): ")
jam_masuk = int(input("Masukkan jam masuk: "))
jam_keluar = int(input("Masukkan jam keluar: "))

# Menghitung lama parkir
lama_parkir = jam_keluar - jam_masuk

# Memanggil function
total = hitung_biaya_parkir(jenis, lama_parkir)

# Menampilkan hasil
print("\nHasil Parkir")
print("Jenis kendaraan :", jenis)
print("Jam masuk       :", jam_masuk)
print("Jam keluar      :", jam_keluar)
print("Lama parkir     :", lama_parkir, "jam")
print("Total biaya     : Rp", total)