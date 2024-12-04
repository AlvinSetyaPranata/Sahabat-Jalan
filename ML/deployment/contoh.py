# recommendation/main.py
import numpy as np
from recommender import load_resources, get_recommendations
from utils import load_data  # Asumsi Anda memiliki fungsi load_data untuk memuat places_df

# Memuat resources (model dan scaler)
model, scaler_user, scaler_item, scaler_target = load_resources()

# Memuat data tempat wisata (misalnya dari file CSV atau database)
_, places_df = load_data()

# Vektor pengguna (untuk user baru beri nilai 5 pada kategori yang sesuai preferensi user)
user_vec = np.array([
    5.0,  # bahari
    5.0,  # budaya
    0.0,  # cagar_alam
    0.0,  # pusat_perbelanjaan
    0.0,  # taman_hiburan
    0.0   # tempat_ibadah
])

# Jumlah rekomendasi yang diinginkan
num_recommendations = 3

# Memanggil fungsi untuk mendapatkan rekomendasi
recommendations = get_recommendations(user_vec, places_df, model, scaler_user, scaler_item, scaler_target, num_recommendations)

# Menampilkan hasil rekomendasi, hasilnya berupa id tempat wisata
print(recommendations)
