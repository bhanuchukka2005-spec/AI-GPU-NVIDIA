import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

# =====================================================
# 1. LOAD DATASET
# =====================================================

IMG_SIZE = (150, 150)
BATCH_SIZE = 32

train_ds = tf.keras.utils.image_dataset_from_directory(
    "seg_train",
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True
)

test_ds = tf.keras.utils.image_dataset_from_directory(
    "seg_test",
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

class_names = train_ds.class_names

print("\nClasses:")
print(class_names)

# =====================================================
# 2. SPEED UP DATA LOADING
# =====================================================

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.prefetch(buffer_size=AUTOTUNE)

# =====================================================
# 3. BUILD CNN MODEL
# =====================================================

model = tf.keras.Sequential([

    tf.keras.Input(shape=(150, 150, 3)),

    tf.keras.layers.Rescaling(1./255),

    tf.keras.layers.Conv2D(
        32,
        (3, 3),
        activation='relu'
    ),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Conv2D(
        64,
        (3, 3),
        activation='relu'
    ),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Conv2D(
        128,
        (3, 3),
        activation='relu'
    ),
    tf.keras.layers.MaxPooling2D(),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(
        256,
        activation='relu'
    ),

    tf.keras.layers.Dropout(0.5),

    tf.keras.layers.Dense(
        6,
        activation='softmax'
    )
])

# =====================================================
# 4. COMPILE MODEL
# =====================================================

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("\nModel Summary:")
model.summary()

# =====================================================
# 5. TRAIN MODEL
# =====================================================

history = model.fit(
    train_ds,
    epochs=10,
    validation_data=test_ds
)

# =====================================================
# 6. EVALUATE MODEL
# =====================================================

test_loss, test_accuracy = model.evaluate(test_ds)

print("\nTest Accuracy:", test_accuracy)
print("Test Loss:", test_loss)

# =====================================================
# 7. PLOT ACCURACY GRAPH
# =====================================================

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend(["Train", "Validation"])

# =====================================================
# 8. PLOT LOSS GRAPH
# =====================================================

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title("Model Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend(["Train", "Validation"])

plt.tight_layout()
plt.show()

# =====================================================
# 9. MAKE PREDICTIONS
# =====================================================

y_true = np.concatenate(
    [labels for images, labels in test_ds],
    axis=0
)

predictions = model.predict(test_ds)

y_pred = np.argmax(predictions, axis=1)

# =====================================================
# 10. CONFUSION MATRIX
# =====================================================

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_true, y_pred))

# =====================================================
# 11. CLASSIFICATION REPORT
# =====================================================

print("\nClassification Report:\n")

print(
    classification_report(
        y_true,
        y_pred,
        target_names=class_names
    )
)

# =====================================================
# 12. DISPLAY SAMPLE PREDICTIONS
# =====================================================

plt.figure(figsize=(12, 8))

for images, labels in test_ds.take(1):

    preds = model.predict(images)
    pred_labels = np.argmax(preds, axis=1)

    for i in range(9):

        plt.subplot(3, 3, i + 1)

        plt.imshow(images[i].numpy().astype("uint8"))

        plt.title(
            f"P: {class_names[pred_labels[i]]}\n"
            f"A: {class_names[labels[i]]}"
        )

        plt.axis("off")

plt.tight_layout()
plt.show()