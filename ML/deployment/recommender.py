# recommendation/recommender.py
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import register_keras_serializable
import numpy as np
import pickle
from utils import load_data

@register_keras_serializable()
def l2_normalize(x, axis=None):
    import tensorflow as tf
    return tf.linalg.l2_normalize(x, axis=1)

def load_resources(model_path='model.h5', scaler_user_path='scalerUser.pkl', scaler_item_path='scalerItem.pkl', scaler_target_path='scalerTarget.pkl'):
    custom_objects = {'l2_normalize': l2_normalize}
    model = load_model(model_path, custom_objects=custom_objects)
    
    # Memuat scaler
    with open(scaler_user_path, 'rb') as f:
        scaler_user = pickle.load(f)
    with open(scaler_item_path, 'rb') as f:
        scaler_item = pickle.load(f)
    with open(scaler_target_path, 'rb') as f:
        scaler_target = pickle.load(f)

    return model, scaler_user, scaler_item, scaler_target

def gen_user_vecs(user_vec, num_items):
    """ Menghasilkan matriks prediksi pengguna untuk mencocokkan ukuran vektor item """
    user_vecs = np.tile(user_vec, (num_items, 1))
    return user_vecs

def get_recommendations(user_vec, places_df, model, scaler_user, scaler_item, scaler_target, num_recommendation=5):
    user_vecs = gen_user_vecs(user_vec, len(places_df))
    
    # Menghilangkan kolom ID dan nama tempat dari data tempat wisata
    places_df_unscaled = places_df.drop(places_df.columns[:2], axis=1)

    # Melakukan normalisasi vektor pengguna dan item
    suser_vecs = scaler_user.transform(user_vecs)
    sitem_vecs = scaler_item.transform(places_df_unscaled)

    # Prediksi rating
    y_p = model.predict([suser_vecs, sitem_vecs])

    # Menggunakan scaler untuk mengembalikan prediksi ke skala asli
    y_pu = scaler_target.inverse_transform(y_p)

    # Menambahkan kolom prediksi rating ke dataframe tempat
    places_df['Predicted_Rating'] = y_pu

    result_df = places_df

    # Mengurutkan berdasarkan rating tertinggi
    result_df_sorted = result_df.sort_values(by='Predicted_Rating', ascending=False)

    return result_df_sorted['Place_Id'].head(num_recommendation)  # Menampilkan n rekomendasi teratas
