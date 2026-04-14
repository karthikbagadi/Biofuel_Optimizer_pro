# 🌿 BioFuel Optimizer Pro

**AI-Based Simulation and Optimization of Biofuel Production from Agri Residues**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style](https://img.shields.io/badge/Code%20Style-PEP%208-yellow.svg)](https://www.python.org/dev/peps/pep-0008/)

---

## 📌 Project Overview

**BioFuel Optimizer Pro** is an AI-powered web application that predicts biofuel yield from agricultural residues (corn straw, rice husk, sugarcane bagasse) and automatically finds optimal process parameters to maximize yield.

The system uses **4 different Machine Learning models** (Random Forest, XGBoost, Gradient Boosting, Neural Network) and **optimization algorithms** (Differential Evolution, Genetic Algorithm, Particle Swarm) to achieve 96% prediction accuracy and 30% yield improvement.

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| 🔮 **Multi-Model Prediction** | Compare predictions from 4 different AI models side by side |
| ⚡ **Parameter Optimization** | Automatically find optimal parameters using Differential Evolution |
| 📊 **Interactive Dashboard** | Real-time visualizations with Plotly |
| 🔬 **SHAP Explainability** | Understand why each prediction is made |
| 📁 **Smart File Upload** | Upload CSV files with auto column detection |
| 📄 **PDF Reports** | Generate professional PDF reports |
| 📱 **WhatsApp Sharing** | Share results instantly on WhatsApp |
| 🎨 **3D Visualizations** | Interactive 3D plots for parameter interactions |
| ⭐ **Favorites** | Save and load favorite parameter combinations |
| 📜 **Prediction History** | Track all past predictions with filters |

---

## 📊 Results Achieved

| Metric | Value |
|--------|-------|
| **Best Model** | Random Forest |
| **R² Score** | 0.96 |
| **MAE** | 1.18 g/L |
| **Yield Improvement** | +30.2% |
| **Time Reduction** | 4-6 weeks → 2-3 seconds |
| **Cost** | $0 (vs $5000-10000 traditional) |

### Feature Importance
- 🧬 **Enzyme Volume**: 61.7% (Most Important)
- ⏰ **Time**: 12.9%
- 🧫 **Substrate**: 10.4%
- 🌡️ **Temperature**: 7.7%
- 🧪 **Inoculum**: 7.3%

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| **Programming Language** | Python 3.10+ |
| **Web Framework** | Streamlit 1.28.1 |
| **Machine Learning** | Scikit-learn, XGBoost, TensorFlow |
| **Optimization** | SciPy (Differential Evolution) |
| **Visualization** | Plotly, Matplotlib, Seaborn |
| **Explainability** | SHAP |
| **PDF Generation** | FPDF |
| **Database** | SQLite3 |
| **IDE** | VS Code, Google Colab |
| **Version Control** | Git, GitHub |

---
## 📁 Project Structure

Biofuel_Optimizer_Pro/
│
├── app.py                      # Main Streamlit application (4500+ lines)
├── train_models.py             # Model training script
├── optimization.py             # Optimization algorithms
├── requirements.txt            # Python dependencies
│
├── data/
│   └── biofuel_data.csv        # Dataset (5000 samples)
│
├── models/                     # Trained models (.pkl files)
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│   ├── gradient_boosting.pkl
│   └── neural_network.pkl
│
├── results/                    # Output reports and figures
│   ├── figures/
│   └── reports/
│
├── src/                        # Source modules
│   ├── data/
│   ├── models/
│   ├── optimization/
│   └── visualization/
│
└── README.md                   # Project documentation

## 🚀 Installation and Setup

### Prerequisites

- Python 3.10 or higher
- Git (optional)

### Step 1: Clone the Repository

git clone https://github.com/karthikbagadi/Biofuel_Optimizer_pro
cd Biofuel-Optimizer-Pro

### Step 2: Create Virtual Environment

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

### Step 3: Install Dependencies

pip install -r requirements.txt

### Step 4: Train Models (First Time Only)

python train_models.py

This will:
- Generate 5000 synthetic samples
- Train all 4 machine learning models
- Save models in the models/ folder

### Step 5: Run the Application

streamlit run app.py

Open your browser and go to: http://localhost:8501

## 📖 How to Use

### 1. Dashboard
View key metrics, yield distribution, and correlation matrix.

### 2. File Upload
Upload your own CSV file. The AI automatically detects column names.

### 3. Predict
- Select prediction mode (Single Model / Compare All / Ensemble)
- Adjust 6 parameter sliders
- Click "Generate Predictions"
- View results from all 4 models

### 4. Optimize
- Select optimization algorithm
- Set iterations and population size
- Click "Run Optimization"
- Get optimal parameters and yield improvement

### 5. Analysis
- View feature importance chart
- Explore SHAP explainability plots
- PCA and clustering analysis

### 6. Reports
- Export results as PDF, Excel, CSV, or JSON
- Share on WhatsApp

## 📸 Screenshots

| Dashboard | Predict Page |
|-----------|--------------|
| (Add screenshot here<img width="1918" height="1026" alt="Screenshot 2026-04-10 172652" src="https://github.com/user-attachments/assets/1013d0b8-b717-466c-99aa-259bf2b318d8" />
<img width="1910" height="1030" alt="Screenshot 2026-04-10 172505" src="https://github.com/user-attachments/assets/856fa0a3-f644-4998-82db-3c8eeb932e21" />
) | (<img width="1919" height="1028" alt="Screenshot 2026-04-10 172921" src="https://github.com/user-attachments/assets/1cfd9408-607c-4ace-a3df-1981a765a4d6" />
![Uploading Screenshot 2026-04-10 172652.png…]()
Add screenshot here) |

| Optimization | Reports Page<img width="1915" height="1027" alt="Screenshot 2026-04-10 173003" src="https://github.com/user-attachments/assets/83917ee5-7e56-4d4b-b6d0-f2b558e9778e" />
 |
|--------------|----------------|
| (Add scre![Uploading Screenshot 2026-04-10 172921.png…]()
enshot here) | (Add screenshot here) |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

| Name | Registration No | VTU No |
|------|-----------------|--------|
| Bagadi Karthik | 22UECM0020 | VTU22064 |
| Nukala Syam Venkata Dhanush | 22UECM0187 | VTU22522 |

Supervisor: Dr. S. Durai, Associate Professor, Department of Computer Science and Engineering

## 📚 References

1. Kuila, A., & Kumar, D. (2025). Optimizing Biofuel Production with Artificial Intelligence. John Wiley & Sons.
2. Hassan, M. M., et al. (2025). Enhancing Prediction of Bioenergy Yield using AI-based Identification of Biomass Species. IEEE ICMISI.
3. Kazmi, A., et al. (2025). Innovations in bioethanol production. Energy Strategy Reviews, 57, 101634.
4. Mafat, I. H., et al. (2024). Machine learning and artificial intelligence for algal cultivation and biofuel production optimization. Springer.
5. Saju, L., et al. (2025). Artificial intelligence and machine intelligence for modeling of bioenergy production. Elsevier.
6. Patidar, S. K., & Raheman, H. (2023). An AI-based approach to improve fuel properties. Biofuels, 14(6), 619-633.

## 🙏 Acknowledgments

- Vel Tech Rangarajan Dr. Sagunthala R&D Institute of Science and Technology
- Department of Computer Science and Engineering
- Dr. S. Durai for continuous guidance and support

## 📧 Contact

For any queries, please contact:
- Bagadi Karthik: [bkarthikbagadi143@gmail.com]
- Nukala Syam Venkata Dhanush: [nukaladhanush223@gmail.com]

⭐ If you find this project useful, please give it a star on GitHub!

