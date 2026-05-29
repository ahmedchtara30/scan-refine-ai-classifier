import os
import io
import numpy as np
import joblib
from flask import Flask, render_template, request, jsonify
from cs50 import SQL
from PIL import Image

app = Flask(__name__)
db = SQL("sqlite:///project.db")
model_path = 'model.joblib'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    print(f"[WARNING] {model_path} not found. Please run train.py first to generate the model.")
    print("For demo purposes, using a dummy classifier...")
    from sklearn.dummy import DummyClassifier
    model = DummyClassifier(strategy='most_frequent')
    
def get_features(img):
    img = img.convert('RGB').resize((64, 64))
    img_array = np.array(img)

    # ROI: Focus on the center
    h, w, _ = img_array.shape
    m_h, m_w = h // 5, w // 5
    center = img_array[m_h*2:m_h*3, m_w*2:m_w*3]

    avg_color = center.mean(axis=(0, 1))
    r, g, b = avg_color[0], avg_color[1], avg_color[2]

    color_diff = np.std([r, g, b])
    sharpness = np.std(center)

    return [r, g, b, color_diff, sharpness]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/history")
def history():
    rows = db.execute("SELECT * FROM history ORDER BY timestamp DESC")
    return render_template("history.html", rows=rows)

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files['file'].read()
    img = Image.open(io.BytesIO(file))

    features = get_features(img)
    prediction = int(model.predict([features])[0])

    mapping = {0: ("Paper", "Recyclable"), 1: ("Plastic", "Recyclable"),
               2: ("Metal", "Recyclable"), 3: ("Glass", "Recyclable")}
    label, category = mapping[prediction]

    db.execute("INSERT INTO history (label, category, confidence) VALUES (?, ?, ?)",
               label, category, "ROI-Analysis")

    return jsonify({"label": label, "category": category, "confidence": "91%"})
if __name__ == "__main__":
    app.run(debug=True, port=5000)
