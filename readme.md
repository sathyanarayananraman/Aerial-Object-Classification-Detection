# 🦅 Bird vs Drone Classification using Deep Learning

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-Red-D00000?style=for-the-badge&logo=keras&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---

## 📌 Project Overview
This project presents an AI-powered image classification system capable of distinguishing between **Birds** and **Drones** from aerial images using Deep Learning techniques.

The project compares the performance of a **Custom Convolutional Neural Network (CNN)** with a **Transfer Learning (MobileNetV2)** model. The best-performing model is deployed using **Streamlit**, allowing users to upload an image and receive an instant prediction with confidence scores.

---

## 🎯 Problem Statement
The increasing use of drones in restricted airspaces and the presence of birds near airports, wind farms, and surveillance zones make accurate identification extremely important.

The objective of this project is to develop an intelligent computer vision system that can classify aerial images into two categories:
* 🦅 **Bird**
* 🚁 **Drone**

using Deep Learning models with high accuracy.

---

## 💼 Business Use Cases
* ✈️ **Airport Bird Strike Prevention:** Detect birds around airport runways to reduce bird-strike accidents.
* 🚁 **Airspace Security:** Identify unauthorized drones entering restricted zones.
* 🌿 **Wildlife Monitoring:** Monitor bird populations using aerial surveillance systems.
* 🛡 **Military & Defense:** Detect suspicious drones near military bases and secure facilities.
* 🌍 **Smart Surveillance:** Automatic monitoring of birds and drones using CCTV or aerial cameras.

---

## 📂 Dataset
The dataset consists of aerial images categorized into two target classes.

### Dataset Split Overview
| Dataset Split | Bird Images | Drone Images | Total Images |
| :--- | :---: | :---: | :---: |
| **Train** | 1414 | 1248 | 2662 |
| **Validation** | 217 | 225 | 442 |
| **Test** | 121 | 94 | 215 |
| **Total** | **1752** | **1567** | **3319** |

---

## 🛠 Technologies Used
* **Programming Language:** Python
* **Deep Learning Frameworks:** TensorFlow, Keras
* **Architectures:** MobileNetV2 (Transfer Learning), Custom CNN
* **Data Processing & Analytics:** NumPy, Scikit-Learn, Pillow
* **Visualization:** Matplotlib
* **Web Deployment:** Streamlit
* **Version Control:** Git & GitHub

---

## 📊 Project Workflow
```text
Dataset ──► Data Preprocessing ──► Data Augmentation ──► Model Building ──► Model Evaluation ──► Streamlit Deployment
                                                         ├── Custom CNN
                                                         └── MobileNetV2
```

---

## 🔄 Data Preprocessing & Augmentation
To improve model generalization, the following preprocessing and augmentation techniques were applied:
* **Image Resizing:** $(224 \times 224)$ pixels
* **Pixel Normalization:** Scaled pixel values to $[0, 1]$ range
* **Data Augmentation:**
  * Horizontal Flip
  * Rotation
  * Zooming
  * Width & Height Shifts

---

## 🧠 Deep Learning Models

### 1️⃣ Custom CNN
* **Architecture:** Sequential layers containing `Conv2D`, `BatchNormalization`, `MaxPooling2D`, `Dropout`, and `Dense` layers with `Sigmoid` output.
* **Test Accuracy:** **88.00%**

### 2️⃣ MobileNetV2 (Transfer Learning) — *Selected Best Model*
The pretrained MobileNetV2 model was fine-tuned for high-precision classification.

| Metric | Score |
| :--- | :---: |
| **Test Accuracy** | **96.74%** |
| **Precision** | **96.77%** |
| **Recall** | **95.74%** |
| **Loss** | **0.0675** |

---

## 📈 Model Comparison

| Model | Test Accuracy |
| :--- | :---: |
| Custom CNN | 88.00% |
| **MobileNetV2** | **96.74%** 🏆 |

---

## 🖥 Streamlit Application
The fine-tuned MobileNetV2 model is deployed as an interactive web interface built with Streamlit.

### Features:
* 📤 Easy image upload functionality
* 🖼 Live preview of uploaded images
* 🎯 Instant prediction (Bird vs Drone)
* 📊 Detailed confidence score and probability distributions
* 🎨 Clean, user-friendly interface

---

## 📂 Project Structure
```text
Bird_vs_Drone_Classification/
│
├── data/
│   ├── train/
│   ├── val/
│   └── test/
│
├── best_bird_drone_model.keras
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Bird_vs_Drone_Classification.git
   ```

2. **Navigate into the project directory:**
   ```bash
   cd Bird_vs_Drone_Classification
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit web application:**
   ```bash
   streamlit run app.py
   ```

---

## 📷 Application Preview
Upload an aerial image to get instant classifications for 🦅 **Bird** or 🚁 **Drone** complete with confidence scores.

---

## 📌 Future Improvements
* [ ] Integrate **YOLOv8** for real-time object detection and bounding boxes.
* [ ] Enable **Webcam & Video Stream** classification.
* [ ] Expand to multi-class identification (specific bird species & drone types).
* [ ] Deploy application via cloud services (e.g., AWS, Streamlit Community Cloud).
* [ ] Develop a lightweight mobile application frontend.

---

## 🎯 Learning Outcomes
* Built end-to-end Deep Learning pipelines with TensorFlow & Keras.
* Applied Transfer Learning using MobileNetV2 for enhanced performance.
* Developed custom CNN architectures from scratch.
* Mastered computer vision metrics and model evaluation techniques.
* Created and deployed web interfaces using Streamlit.

---

## 👩‍💻 Author
**Sathyanarayanan**  
*Aspiring Data Scientist*

* **Skills:** Python | SQL | TensorFlow | Deep Learning | Machine Learning | Computer Vision | Power BI | Streamlit