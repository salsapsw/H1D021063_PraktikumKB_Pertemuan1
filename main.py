import math
import datetime
import locale

# Set bahasa lokal ke Indonesia
locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')

def main():
    # ini library datetime
    sekarang = datetime.datetime.now()
    # ngatur format waktu jadi "17 Maret 2025" dalam bahasa Indonesia
    waktu_formatted = sekarang.strftime("%d %B %Y")
    jam_formatted = sekarang.strftime("%H:%M:%S")

    # ini implementasi struktur kontrol if-elif-else buat nentuin ucapan dan motivasi
    jam = sekarang.hour
    if jam < 12:
        ucapan = "pagi"
        motivasi = "Semangat beraktivitas! Jangan lupa sarapan biar kuat seharian! 🌞"
    elif jam < 15:
        ucapan = "siang"
        motivasi = "Tetap fokus dan jangan lupa istirahat sebentar ya! 💪"
    elif jam < 18:
        ucapan = "sore"
        motivasi = "Waktunya bersantai sejenak setelah seharian beraktivitas! ☕"
    else:
        ucapan = "malam"
        motivasi = "Istirahat yang cukup dan siapkan energi untuk besok! 🌙"

    print(f"Halo, selamat {ucapan}! Sekarang tanggal {waktu_formatted}, pukul {jam_formatted}.")
    print(motivasi, "\n")

    # ini implementasi struktur data list
    angka_list = [1, 3, 6, 8, 10]

    # ini implementasi struktur data dictionary buat nyimpan hasil kuadrat dari data yang ada di list
    hasil_kuadrat = {}

    # ini implementasi struktur kontrol for loop untuk menghitung kuadrat
    for angka in angka_list:
        kuadrat = math.pow(angka, 2)  # ambil dari library math untuk menghitung pangkat 2
        hasil_kuadrat[angka] = kuadrat

    print("Hasil kuadrat dari setiap angka dalam list:")
    # ini implementasi struktur kontrol perulangan for loop
    for key, value in hasil_kuadrat.items():
        print(f"Kuadrat {key} = {value}")

if __name__ == '__main__':
    main()
