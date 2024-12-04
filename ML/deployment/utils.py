import pandas as pd

def load_data():
    # Membaca file CSV
    destination_df = pd.read_csv('./data/tourism_with_id.csv')  # Data destinasi
    tourism_rating_df = pd.read_csv('./data/tourism_rating.csv')  # Data rating wisata
    user_df = pd.read_csv('./data/user.csv')  # Data pengguna

    # Menggabungkan data pengguna dengan rating dan destinasi berdasarkan User_Id dan Place_Id
    merged_df = pd.merge(user_df, tourism_rating_df, on='User_Id', how='inner')
    merged_df = pd.merge(merged_df, destination_df, on='Place_Id')

    # Menghitung statistik pengguna: rata-rata rating dan usia
    user_stats = merged_df.groupby('User_Id').agg(
        rating_avg=('Place_Ratings', 'mean'),  # Rata-rata rating per user
        age=('Age', 'first')                   # Usia pertama kali muncul per user
    ).reset_index()

    # Menghitung rata-rata rating per kategori untuk setiap user
    category_avg = merged_df.pivot_table(
        index='User_Id',
        columns='Category',                      # Kolom kategori
        values='Place_Ratings',                   # Kolom rating tempat
        aggfunc='mean',                           # Fungsi rata-rata
        fill_value=0                              # Mengisi nilai kosong dengan 0
    ).reset_index()

    # Menggabungkan statistik pengguna dengan rata-rata rating per kategori
    user_data = pd.merge(user_stats, category_avg, on='User_Id')

    # Menghapus kolom yang tidak diperlukan dari destination_df
    places_df = destination_df.drop([
        'Price','Description', 'City', 'Coordinate', 'Lat', 
        'Long', 'Time_Minutes', 'Unnamed: 11', 'Unnamed: 12'
    ], axis=1)
    
    # Mengkodekan kategori menjadi variabel dummy (One-hot encoding)
    encoded_places_df = pd.get_dummies(places_df, columns=['Category'], prefix='Category')

    # Mengembalikan dua DataFrame: user_data dan encoded_places_df
    return user_data, encoded_places_df
