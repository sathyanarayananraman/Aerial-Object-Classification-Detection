🦅 Bird vs Drone Classification using Deep Learning
📌 Project Overview
This project presents an AI-powered image classification system capable of distinguishing between Birds and Drones from aerial images using Deep Learning techniques.

The project compares the performance of a Custom Convolutional Neural Network (CNN) with a Transfer Learning MobileNetV2 model. The best-performing model is deployed using Streamlit, allowing users to upload an image and receive an instant prediction with confidence scores.

🎯 Problem Statement
The increasing use of drones in restricted airspaces and the presence of birds near airports, wind farms, and surveillance zones make accurate identification extremely important.

The objective of this project is to develop an intelligent computer vision system that can classify aerial images into two categories:

🦅 Bird
🚁 Drone
using Deep Learning models with high accuracy.

💼 Business Use Cases
✈️ Airport Bird Strike Prevention
Detect birds around airport runways to reduce bird-strike accidents.

🚁 Airspace Security
Identify unauthorized drones entering restricted zones.

🌿 Wildlife Monitoring
Monitor bird populations using aerial surveillance systems.

🛡 Military & Defense
Detect suspicious drones near military bases and secure facilities.

🌍 Smart Surveillance
Automatic monitoring of birds and drones using CCTV or aerial cameras.

📂 Dataset
Classification Dataset
Classes

Bird
Drone
Dataset Split
Dataset	Bird	Drone
Train	1414	1248
Validation	217	225
Test	121	94
Total Images: 3319

🛠 Technologies Used
Python
TensorFlow
Keras
MobileNetV2
Custom CNN
NumPy
Matplotlib
Scikit-Learn
Pillow
Streamlit
GitHub
📊 Project Workflow
Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Data Augmentation
      │
      ▼
Custom CNN
      │
      ▼
MobileNetV2
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Comparison
      │
      ▼
Save Best Model
      │
      ▼
Streamlit Deployment
🔄 Data Preprocessing
The following preprocessing techniques were applied:

Image Resizing (224 × 224)
Pixel Normalization
Image Augmentation
Horizontal Flip
Rotation
Zoom
Width Shift
Height Shift
🧠 Deep Learning Models
1️⃣ Custom CNN
Architecture

Conv2D
Batch Normalization
MaxPooling
Dropout
Dense Layer
Sigmoid Output
Performance
Metric	Value
Accuracy	88%
2️⃣ MobileNetV2 (Transfer Learning)
The pretrained MobileNetV2 model was fine-tuned using transfer learning.

Performance
Metric	Value
Test Accuracy	96.74%
Precision	96.77%
Recall	95.74%
Loss	0.0675
📈 Model Comparison
Model	Accuracy
Custom CNN	88.00%
MobileNetV2	96.74%
🏆 Best Model: MobileNetV2

📊 Evaluation Metrics
The following evaluation metrics were used:

Accuracy
Precision
Recall
F1 Score
Confusion Matrix
Classification Report
Training Accuracy Curve
Validation Accuracy Curve
Training Loss Curve
Validation Loss Curve
🖥 Streamlit Application
The trained MobileNetV2 model was deployed using Streamlit.

Features
Upload Image
Image Preview
Bird / Drone Prediction
Confidence Score
Probability Scores
Professional User Interface
📂 Project Structure
Bird_vs_Drone_Classification/

│
├── data/
│   ├── train/
│   ├── val/
│   └── test/
│
├── best_bird_drone_model.keras
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── screenshots/
🚀 Installation
Clone the repository

git clone https://github.com/yourusername/Bird_vs_Drone_Classification.git
Move into the project folder

cd Bird_vs_Drone_Classification
Install dependencies

pip install -r requirements.txt
Run the Streamlit application

streamlit run app.py
📷 Application Preview
Upload an aerial image.

The application predicts

🦅 Bird
🚁 Drone
along with confidence scores.

📌 Future Improvements
YOLOv8 Object Detection
Real-Time Webcam Detection
Video Classification
Multi-Class Bird Species Detection
Cloud Deployment
Mobile Application
🎯 Learning Outcomes
Through this project, I gained practical experience in

Deep Learning
Image Classification
Transfer Learning
TensorFlow
CNN Architecture
MobileNetV2
Computer Vision
Streamlit Deployment
Model Evaluation
GitHub Project Management
👩‍💻 Author
Sathyanarayanan

Aspiring Data Scientist

Skills
Python
SQL
TensorFlow
Deep Learning
Machine Learning
Computer Vision
Power BI
Streamlit


