import tensorflow as tf
import numpy as np

# Datos
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# Modelo: una neurona
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])

# Entrenamiento
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(celsius, fahrenheit, epochs=500)

print(model.predict(np.array([[100.0]])))
