ScanRefine: A Recycling Classifier

Video Demo: https://www.youtube.com/watch?v=3sz7NQcCQW4

1. Project Overview

ScanRefine is a full-stack web application created to help users sort everyday household waste into four main recycling categories: Paper, Plastic, Metal, and Glass. The idea is simple from the user’s point of view: upload a photo of an item, and the system tells you where it belongs.

the application combines a Flask web interface with a K-Nearest Neighbors (KNN) machine learning model. When an image is uploaded, it goes through a custom feature-extraction process before being classified. The result is returned almost instantly.

The motivation for this project was to connect machine learning concepts with something practical and useful. Recycling mistakes are common, and even small errors can cause contamination. ScanRefine shows how basic computer vision techniques can help reduce that problem. Instead of relying on external APIs or heavy cloud services, the entire system is built using open-source Python libraries, which keeps it lightweight, transparent, and easy to run locally.

2. File Structure and Functionality

The project is organized into several files, each with a clear and specific role:

app.py
This file is the core of the application. It runs the Flask backend, manages routes, handles image uploads, and communicates with the SQLite database. It also includes the feature-extraction logic used during prediction. Keeping this logic identical to the training phase was essential to maintain consistent results.

train.py
This script is responsible for training the model. It scans the dataset/ directory, processes images from a Kaggle dataset, extracts features, and trains the KNN classifier. Once training is complete, the model is saved as model.joblib. This file represents the learning phase of the project.

model.joblib
A serialized version of the trained KNN model. Loading this file allows the application to make predictions immediately, without retraining every time the app runs. This significantly improves performance and reduces CPU usage.

project.db
A SQLite database used to store the history of user scans. It keeps records of predictions along with timestamps, making the app persistent rather than temporary.

templates/index.html & history.html
These files make up the frontend. The main page (index.html) allows users to upload images, while history.html displays previous scans using data retrieved from the database and rendered with Jinja2.

requirements.txt
A list of all required Python libraries, such as Flask, NumPy, Pillow, and scikit-learn, to ensure the project can be run easily in a clean environment.

3. Data Strategy

The machine learning model was trained using a public dataset from Kaggle, which provided a large number of labeled recycling images. This helped establish a solid baseline for classification.

A key part of the project, however, was feature engineering. Instead of feeding raw images directly into the model—which would be inefficient and memory-intensive—I designed a custom feature-extraction method.

Each image is reduced to five numerical features:

Average Red intensity

Average Green intensity

Average Blue intensity

Saturation variance

Edge sharpness

This approach dramatically reduces the size of the data while still preserving enough information to distinguish between materials. As a result, the model runs quickly and can operate on low-power systems.

4. Design Choices and Engineering Challenges

While developing ScanRefine, several real-world problems appeared that required practical solutions rather than textbook answers.

During early testing, metal objects such as aluminum trays or cutlery were often misclassified as paper. The reason became clear after investigation: both materials have high brightness values across the RGB channels, which makes them appear very similar numerically.

To address this, I introduced a weighted saturation calculation. Metal surfaces tend to be almost colorless, reflecting light without much variation between color channels. Paper, even when white, usually contains slight color differences due to texture, ink, or lighting. By emphasizing the variance between RGB channels, the model became much better at separating metallic objects from paper.

Background Interference and Image Cropping

Another issue was background noise. For example, when a plastic bottle was photographed on a patterned surface, the background colors sometimes influenced the prediction more than the object itself.

Instead of using heavy background-removal models, which would be inefficient in the CS50 environment, I chose a simpler solution. The image is automatically cropped to the central 40%, which is the area most likely to contain the object. This reduced background interference and noticeably improved accuracy in everyday scenarios.

5. Database Integration

I integrated a SQLite database into the application. Each scan is stored with its predicted category and a timestamp.

This decision helped transform ScanRefine from a simple demo into a functional tool. Users can review their past scans, which adds an educational aspect and encourages better recycling habits over time. The database operations are handled using the CS50 Python library, which simplifies SQL queries and helps prevent common security issues such as SQL injection.
