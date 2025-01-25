import tensorflow as tf

# Define the paths
hdf5_model_path = "models\keypoint_classifier_19th_Jan.h5"  # Replace with your HDF5 file path
tflite_model_path = "models\keypoint_classifier_19th_Jan.tflite"  # Replace with desired save path for the TFLite model

# Load the HDF5 model
model = tf.keras.models.load_model(hdf5_model_path)

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TensorFlow Lite model
with open(tflite_model_path, "wb") as f:
    f.write(tflite_model)

print(f"TFLite model saved to {tflite_model_path}")
