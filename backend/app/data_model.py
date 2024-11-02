# Run this file to start the backend
import pandas as pd
import numpy as np
import os 
import time
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

model_path = "data_model.keras"

def create_and_train_model():
    data = pd.read_csv("Student_performance_data _.csv")

    data.drop('StudentID', axis=1, inplace=True)
    data.drop('GradeClass', axis=1, inplace=True)

    print(data.head())

    data_labels = data.pop("GPA")
    data_features = np.array(data.copy())

    X_train, X_test, y_train, y_test = train_test_split(data_features, data_labels, test_size=0.1, random_state=42)

    normalize = layers.Normalization()
    normalize.adapt(data_features)

    data_model = tf.keras.Sequential([
        normalize,
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

    data_model.compile(loss=tf.keras.losses.MeanSquaredError(),
                    optimizer=tf.keras.optimizers.Adam(),
                    metrics=['mean_squared_error'])

    data_model.fit(X_train, y_train, epochs=10)

    data_model.save(model_path)
    return data_model

def load_model():
    if os.path.exists(model_path):
        return tf.keras.models.load_model(model_path)
    else:
        return create_and_train_model()
    
Neural_Network = load_model()