from tensorflow.keras.models import load_model
from tensorflow.keras.utils import register_keras_serializable
import numpy as np
from sklearn.preprocessing import StandardScaler
from utils import load_data
import pickle

_, places_df = load_data()

@register_keras_serializable()
def l2_normalize(x, axis=None):
    import tensorflow as tf
    return tf.linalg.l2_normalize(x, axis=1)

custom_objects = {'l2_normalize': l2_normalize}
model = load_model('model.h5', custom_objects=custom_objects)

def gen_user_vecs(user_vec, num_items):
    """ given a user vector return:
        user predict maxtrix to match the size of item_vecs """
    user_vecs = np.tile(user_vec, (num_items, 1))
    return user_vecs

with open('scalerUser.pkl', 'rb') as f:
    scalerUser = pickle.load(f)

with open('scalerItem.pkl', 'rb') as f:
    scalerItem = pickle.load(f)

with open('scalerTarget.pkl', 'rb') as f:
    scalerTarget = pickle.load(f)

new_user_id = 5000
new_rating_ave = 0.0
new_bahari = 5.0
new_budaya = 0.0
new_cagar_alam = 0.0
new_pusat_perbelanjaan = 0.0
new_taman_hiburan = 0.0
new_tempat_ibadah = 0.0

user_vec = np.array([
    new_bahari, new_budaya, new_cagar_alam, new_pusat_perbelanjaan,
    new_taman_hiburan, new_tempat_ibadah
])

user_vecs = gen_user_vecs(user_vec,len(places_df))

places_df_unscaled = places_df.drop(places_df.columns[:2], axis=1)

suser_vecs = scalerUser.transform(user_vecs)
sitem_vecs = scalerItem.transform(places_df_unscaled)

y_p = model.predict([suser_vecs, sitem_vecs])

y_pu = scalerTarget.inverse_transform(y_p)

places_df['Predicted_Rating'] = y_pu  # Menambahkan kolom prediksi rating ke places_df

# Menampilkan hasil dengan ID tempat wisata dan nama tempat
result_df = places_df[['Place_Id', 'Place_Name', 'Predicted_Rating']]

# Mengurutkan berdasarkan prediksi rating tertinggi
result_df_sorted = result_df.sort_values(by='Predicted_Rating', ascending=False)

print(result_df_sorted.head(5))


