#Main architecture of the model
import tensorflow as tf
import streamlit as st
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.applications import DenseNet201
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import numpy as np
import os

# weights path
current_dir = os.path.dirname(__file__)
densenet_weights_path = os.path.join(current_dir, '..', 'models', 'model_densenet_masked.weights.h5')

def build_model_tuned_densenet201():
    base_model = DenseNet201(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

    # Freeze the pre-trained layers
    for layer in base_model.layers:
        layer.trainable = False
    for layer in base_model.layers[137:]: # Comment line if not fine tuned
        layer.trainable = True            # Comment line if not fine tuned

    # Add custom classifier layers
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(256, activation='relu')(x)
    x = Dropout(0.2)(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.2)(x)
    output = Dense(3, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=output)

    # Compile the model
    optimizer = Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model

@st.cache_resource()
def load_model(model_name):
    if model_name == 'DenseNet201':
        model = build_model_tuned_densenet201()
        model.load_weights(densenet_weights_path)
        return model
    # Add other models here
    return None

class_names = {
    0: 'COVID',
    1: 'Non COVID',
    2: 'Normal'
}
def prediction (model, image):
    
    prediction = model.predict(image)
    predicted_label = np.argmax(prediction)
    return class_names[predicted_label]