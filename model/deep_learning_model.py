import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# 1️⃣ Load processed data
X_train = np.load("model/X_train.npy")
X_test = np.load("model/X_test.npy")
y_train = np.load("model/y_train.npy")
y_test = np.load("model/y_test.npy")

# 2️⃣ Convert labels to categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# 3️⃣ Build ANN model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(y_train.shape[1], activation='softmax'))

# 4️⃣ Compile model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 5️⃣ Train model
model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_data=(X_test, y_test)
)

# ✅ 6️⃣ SAVE THE TRAINED MODEL (THIS IS THE LINE)
model.save("model/url_attack_model.h5")

print("✅ Model training completed and saved as url_attack_model.h5")
