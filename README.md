# ♻️ ScanRefine — AI-Powered Recycling Classifier

> 🎓 CS50's Introduction to AI with Python | Harvard University (2026)  
> 👨‍💻 Ahmed Chtara | Intelligent Systems & AI Engineer

## 🎥 Live Demo
[![ScanRefine Demo](https://img.youtube.com/vi/3sz7NQcCQW4/0.jpg)](https://youtu.be/3sz7NQcCQW4)  
*Watch the full demo: Upload → Classify → Track History*

## 🎯 What It Does
ScanRefine helps users sort household waste into **4 recycling categories** (Paper, Plastic, Metal, Glass) using computer vision.  
→ **Upload a photo** → Get instant classification + recyclability status.

## 🧠 The Smart Part: Custom Feature Engineering
Instead of heavy deep learning, I engineered **5 lightweight features** for fast, accurate classification on low-power systems:

| Feature | Purpose |
|---------|---------|
| **Avg Red / Green / Blue** | Capture base color signature |
| **Saturation Variance** | Distinguish metal (gray/neutral) from paper (textured) |
| **Edge Sharpness** | Detect material texture differences |

✅ **ROI Cropping**: Auto-crops to center 40% to ignore background noise  
✅ **KNN Classifier (K=3)**: Fast, interpretable, no GPU required  
✅ **SQLite History**: Tracks user scans for educational feedback

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| **Backend** | Python, Flask, scikit-learn, joblib |
| **ML Model** | K-Nearest Neighbors, custom feature extraction |
| **Frontend** | HTML5, Bootstrap 5, Vanilla JavaScript |
| **Database** | SQLite (via CS50 SQL library) |
| **Tools** | Git, GitHub, VS Code, PIL/Pillow, NumPy |

## 📁 Project Structure

scan-refine-ai-classifier/

├── app.py # Flask backend: routes, prediction, DB

├── train.py # Model training script

├── model.joblib # Trained KNN model (serialized)

├── project.db # SQLite database (scan history)

├── requirements.txt # Python dependencies

├── templates/

│ ├── index.html # Main upload UI

│ └── history.html # Scan history page

└── README.md

## 🚀 Run Locally
```bash
# 1. Clone & install
git clone https://github.com/ahmedchtara30/scan-refine-ai-classifier.git
cd scan-refine-ai-classifier
pip install -r requirements.txt

# 2. Train model
python train.py

# 3. Launch app
python app.py
# Open http://localhost:5000 in your browser
```
## 💡 Engineering Challenges Solved

| Problem | Solution |
|---------|----------|
| **Metal vs. Paper confusion** | Weighted saturation variance to detect neutral vs. textured surfaces |
| **Background interference** | ROI cropping to focus on object center (40%) |
| **Performance on low-end devices** | Feature engineering instead of raw-image CNN |

## 📬 Contact & Collaboration
📧 chtaraahmed30@gmail.com | 📍 Tunisia
🔗 LinkedIn | 🌐 Available for remote freelance
Open to: Python automation, ML prototyping, embedded AI projects

Portfolio under active development. Full source available upon request for verified clients.

