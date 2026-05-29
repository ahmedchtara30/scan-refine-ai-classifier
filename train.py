import os
import numpy as np
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
import joblib

def extract_features(image_path):
    img = Image.open(image_path).convert('RGB').resize((64, 64))
    img_array = np.array(img)

    # 1. ROI: Focus on the center (Middle 40%) to ignore kitchen tiles
    h, w, _ = img_array.shape
    m_h, m_w = h // 5, w // 5
    center = img_array[m_h*2:m_h*3, m_w*2:m_w*3]

    # 2. Basic Stats
    avg_color = center.mean(axis=(0, 1))
    r, g, b = avg_color[0], avg_color[1], avg_color[2]

    # 3. Metal Check: How close are R, G, and B? (Metal is perfectly gray)
    # Lower 'diff' means more likely to be metal/glass
    color_diff = np.std([r, g, b])

    # 4. Sharpness: Metal/Plastic have high contrast edges
    sharpness = np.std(center)

    return [r, g, b, color_diff, sharpness]

categories = {"paper": 0, "plastic": 1, "metal": 2, "glass": 3}
X, y = [], []

print("ScanRefine Model...")

for category, label in categories.items():
    folder = f"dataset/{category}"
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            if filename.lower().endswith((".jpg", ".png", ".jpeg")):
                X.append(extract_features(os.path.join(folder, filename)))
                y.append(label)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)
joblib.dump(model, 'model.joblib')
print(" model.joblib ready.")
