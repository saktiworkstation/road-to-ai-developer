import random

# Data menu makanan Indonesia
menu_makanan = [
    {"nama": "Nasi Goreng", "kalori": 300, "protein": 10, "lemak": 8, "karbohidrat": 45, "gula": 3, "serat": 2},
    {"nama": "Ayam Bakar", "kalori": 250, "protein": 20, "lemak": 5, "karbohidrat": 0, "gula": 1, "serat": 0},
    {"nama": "Sayur Asem", "kalori": 100, "protein": 2, "lemak": 1, "karbohidrat": 20, "gula": 5, "serat": 4},
    {"nama": "Soto Ayam", "kalori": 350, "protein": 15, "lemak": 10, "karbohidrat": 30, "gula": 2, "serat": 3},
    {"nama": "Ikan Bakar", "kalori": 200, "protein": 25, "lemak": 8, "karbohidrat": 0, "gula": 1, "serat": 0},
    {"nama": "Capcay", "kalori": 120, "protein": 5, "lemak": 3, "karbohidrat": 20, "gula": 3, "serat": 2},
    {"nama": "Gado-Gado", "kalori": 180, "protein": 8, "lemak": 6, "karbohidrat": 25, "gula": 4, "serat": 5},
    {"nama": "Rendang", "kalori": 400, "protein": 30, "lemak": 15, "karbohidrat": 5, "gula": 1, "serat": 2},
    {"nama": "Pecel Lele", "kalori": 280, "protein": 20, "lemak": 10, "karbohidrat": 15, "gula": 3, "serat": 2},
    {"nama": "Bakso", "kalori": 250, "protein": 15, "lemak": 10, "karbohidrat": 20, "gula": 2, "serat": 1},
    {"nama": "Nasi Uduk", "kalori": 320, "protein": 10, "lemak": 12, "karbohidrat": 40, "gula": 3, "serat": 2},
    {"nama": "Pisang Goreng", "kalori": 150, "protein": 2, "lemak": 5, "karbohidrat": 25, "gula": 10, "serat": 2},
    {"nama": "Sambal Terasi", "kalori": 50, "protein": 1, "lemak": 2, "karbohidrat": 10, "gula": 5, "serat": 1},
    {"nama": "Perkedel Kentang", "kalori": 100, "protein": 3, "lemak": 5, "karbohidrat": 15, "gula": 1, "serat": 2},
    {"nama": "Pecel Sayur", "kalori": 150, "protein": 6, "lemak": 4, "karbohidrat": 20, "gula": 3, "serat": 4},
    {"nama": "Mie Goreng", "kalori": 320, "protein": 8, "lemak": 12, "karbohidrat": 40, "gula": 2, "serat": 1},
    {"nama": "Telur Balado", "kalori": 200, "protein": 10, "lemak": 8, "karbohidrat": 5, "gula": 1, "serat": 1},
    {"nama": "Sayur Lodeh", "kalori": 150, "protein": 4, "lemak": 3, "karbohidrat": 20, "gula": 2, "serat": 3},
    {"nama": "Tahu Goreng", "kalori": 120, "protein": 8, "lemak": 5, "karbohidrat": 10, "gula": 1, "serat": 2},
    {"nama": "Sate Ayam", "kalori": 200, "protein": 20, "lemak": 10, "karbohidrat": 5, "gula": 1, "serat": 0},
    {"nama": "Lalapan", "kalori": 50, "protein": 3, "lemak": 1, "karbohidrat": 10, "gula": 2, "serat": 2},
    {"nama": "Pisang Rebus", "kalori": 100, "protein": 1, "lemak": 0, "karbohidrat": 25, "gula": 10, "serat": 2},
    {"nama": "Jus Alpukat", "kalori": 200, "protein": 2, "lemak": 10, "karbohidrat": 25, "gula": 15, "serat": 4}
    # Tambahkan data menu makanan lainnya di sini
]

# Fungsi untuk menghitung total kandungan gizi menu makanan
def hitung_total_gizi(menu):
    total_gizi = {"kalori": 0, "protein": 0, "lemak": 0, "karbohidrat": 0, "gula": 0, "serat": 0}
    for makanan in menu:
        for nutrient in total_gizi:
            total_gizi[nutrient] += makanan[nutrient]
    return total_gizi

# Fungsi untuk menghasilkan populasi awal menu makanan secara acak
def generate_populasi_awal(pop_size):
    populasi_awal = []
    for _ in range(pop_size):
        menu = random.choices(menu_makanan, k=17)  # Mengambil 7 makanan untuk 1 minggu
        populasi_awal.append(menu)
    return populasi_awal

# Fungsi untuk menghitung fitness dari sebuah individu dalam populasi
def hitung_fitness(menu, target_kalori, target_protein):
    total_gizi = hitung_total_gizi(menu)
    kalori_diff = abs(total_gizi["kalori"] - target_kalori)
    protein_diff = abs(total_gizi["protein"] - target_protein)
    fitness = 1 / (1 + kalori_diff + protein_diff)
    return fitness

# Fungsi untuk melakukan seleksi orangtua menggunakan turnamen
def seleksi_orangtua(populasi, target_kalori, target_protein):
    k = 3  # Jumlah individu yang akan dipertandingkan dalam turnamen
    orangtua = []
    for _ in range(2):  # Memilih 2 orangtua
        peserta_turnamen = random.sample(populasi, k)
        peserta_turnamen_fitness = [(menu, hitung_fitness(menu, target_kalori, target_protein)) for menu in peserta_turnamen]
        peserta_turnamen_fitness.sort(key=lambda x: x[1], reverse=True)
        orangtua.append(peserta_turnamen_fitness[0][0])  # Memilih individu dengan fitness tertinggi
    return orangtua

# Fungsi untuk melakukan crossover dua menu makanan orangtua
def crossover(orangtua1, orangtua2):
    titik_crossover = random.randint(1, len(orangtua1) - 1)
    anak1 = orangtua1[:titik_crossover] + orangtua2[titik_crossover:]
    anak2 = orangtua2[:titik_crossover] + orangtua1[titik_crossover:]
    return anak1, anak2

# Fungsi untuk melakukan mutasi pada menu makanan
def mutasi(menu, mutation_rate):
    for i in range(len(menu)):
        if random.random() < mutation_rate:
            menu[i] = random.choice(menu_makanan)
    return menu

# Fungsi untuk melakukan algoritma genetika
def algoritma_genetika(target_kalori, target_protein, pop_size, mutation_rate, generations):
    populasi = generate_populasi_awal(pop_size)
    for _ in range(generations):
        orangtua1, orangtua2 = seleksi_orangtua(populasi, target_kalori, target_protein)
        anak1, anak2 = crossover(orangtua1, orangtua2)
        anak1 = mutasi(anak1, mutation_rate)
        anak2 = mutasi(anak2, mutation_rate)
        populasi.extend([anak1, anak2])
        populasi = sorted(populasi, key=lambda x: hitung_fitness(x, target_kalori, target_protein), reverse=True)[:pop_size]
    return populasi[0]

# Fungsi untuk menampilkan menu makanan yang dihasilkan
def tampilkan_menu(menu):
    print("Menu Makanan Sehat:")
    for makanan in menu:
        print("- {}".format(makanan["nama"]))

# Input berat badan dan tinggi badan user
berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (cm): "))

# Kalkulasi target kalori dan protein harian berdasarkan berat badan dan tinggi badan
target_kalori = berat_badan * 30  # Asumsi kalori harian adalah 30 kalori per kg berat badan
target_protein = berat_badan * 0.8  # Asumsi protein harian adalah 0.8 gram per kg berat badan

# Menjalankan algoritma genetika untuk menghasilkan menu makanan sehat
menu_makanan_sehat = algoritma_genetika(target_kalori, target_protein, pop_size=20, mutation_rate=0.1, generations=100)

# Menampilkan menu makanan yang dihasilkan
tampilkan_menu(menu_makanan_sehat)