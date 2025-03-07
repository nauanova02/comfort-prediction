# 🌡️ IoT-Based Comfort Prediction System  
**Category:** IoT | Data Analytics | Machine Learning | MQTT | MongoDB | XGBoost  

## **🔹 Overview**  
This project builds an **IoT-driven comfort prediction system** that collects real-time **sensor data** (temperature, humidity, light, and sound) from an **Arduino board connected to a Raspberry Pi**.  
The data is published via **MQTT**, stored in a **MongoDB cloud database**, and then processed using an **XGBoost-based forecasting model** with **lag features** to predict future comfort levels.  

✅ **Real-time sensor data collection & storage** via **Mosquitto MQTT & MongoDB**  
✅ **Feature engineering using lag variables** for time-series forecasting  
✅ **XGBoost prediction model** for temperature, humidity, light, and sound levels  
✅ **Integration with a Flask API for data retrieval & visualization**  

This system enhances **building automation and smart environments**, helping maintain optimal comfort conditions in **offices, classrooms, and industrial facilities**.  

---

## **🛠️ System Architecture**  

### **1️⃣ Sensor Layer (Data Acquisition)**
- **Light Sensor** → Measures **lux (lx)** for ambient brightness  
- **Sound Sensor** → Records **decibels (dB)** for noise levels  
- **Temperature Sensor** → Reads **Celsius (°C)**  
- **Humidity Sensor** → Captures **relative humidity (%)**  
- **Hardware Used:** **Arduino Board + Raspberry Pi**  

📌 **Industry Standards Used for Comfort:**  
| Metric        | Unit  | Standard | Comfortable Range |
|--------------|------|------------------------|----------------|
| Light        | Lux  | IESNA RP-1             | 300-500 lx |
| Sound        | dBA  | ANSI/ASA S12.60-2010   | 30-40 dB |
| Temperature  | °C   | ASHRAE Standard 55-2020 | 20-24°C |
| Humidity     | %    | ASHRAE Standard 55-2020 | 40-60% |

---

### **2️⃣ Communication Layer (MQTT & Security)**
✅ **JavaScript Bridge** → Listens to MQTT topics and **pushes sensor data to MongoDB**  
✅ **Python Bridge** → Reads sensor data from MQTT and **processes it for ML input**  
✅ **Websockets & HTTPS** – Secure transmission of sensor data  
✅ **Security Measures:** **Data encryption, authentication, access control**  

---

### **3️⃣ Data Layer (Database & Processing)**
✅ **MongoDB Cloud Database** – Stores real-time and historical sensor data  
✅ **Data Enrichment** – Enhances records with **timestamps & metadata**  

---

### **4️⃣ Forecasting Layer (Machine Learning Model)**
✅ **XGBoost Model with Lag Features** – Uses historical data for **time-series forecasting**  
✅ **Feature Engineering:** Generates **lag variables (previous sensor values)** to improve prediction accuracy  
✅ **Evaluation Metrics:** RMSE, MAE, R²  

---
## **📈 Model Performance Results (XGBoost)**  

| **Metric**       | **Temperature** | **Humidity** | **Sound** | **Light** |
|-----------------|---------------|------------|--------|-------|
| **RMSE**        | **0.10**       | **0.37**   | **2.71** | **2.58** |
| **R² Score**    | **0.97**       | **0.97**   | **0.86** | **0.53** |
| **MAE**         | **0.06**       | **0.12**   | **1.93** | **1.39** |

📌 **Key Observations:**  
✅ **High accuracy for Temperature & Humidity predictions (R² = 0.97)**  
✅ **Sound prediction shows strong performance (R² = 0.86), but noise variance affects RMSE**  
✅ **Light intensity prediction needs improvement (R² = 0.53) due to external environmental influences**  

### **Example Forecasts for the Next Hour**
📊 **Predicted Environmental Conditions:**
- **Temperature:** 22.5°C → 23.1°C  
- **Humidity:** 50% → 48%  
- **Light Intensity:** 350 lx → 400 lx  
- **Sound Levels:** 35 dBA → 38 dBA  

📌 **Conclusion:**  
Your system **successfully predicts comfort parameters** and provides **actionable insights for smart building automation**.
