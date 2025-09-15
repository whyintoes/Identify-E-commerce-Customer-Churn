# Identify Customer Churn with Machine Learning

## Overview
Proyek ini membangun model machine learning untuk memprediksi customer churn pada perusahaan e-commerce. Churn = pelanggan berhenti menggunakan layanan.

## Goals
- **Business:** Mengurangi churn, meningkatkan retensi, optimalkan biaya.  
- **Analytical:** Bangun model klasifikasi churn, identifikasi faktor penting, pilih metrik evaluasi yang sesuai.

## Dataset
- Sumber: `data_ecommerce_customer_churn.csv`  
- Target: `0 = Tidak Churn`, `1 = Churn`

## Methodology
1. Business & Data Understanding  
2. Data Cleaning & Preparation  
3. Feature Engineering  
4. Modeling (Logistic Regression, KNN, Decision Tree, Random Forest, Gradient Boosting, XGBoost)  
5. Handling imbalance (SMOTE, NearMiss, dll.)  
6. Evaluation (Accuracy, Recall, Precision, F1, ROC-AUC)  
7. Hyperparameter Tuning  

## Evaluation
- Fokus pada **Recall** agar pelanggan berisiko tidak terlewat.  
- Type I Error (FP) → biaya retensi tidak perlu.  
- Type II Error (FN) → kehilangan pelanggan berharga.  

## Business Insight
- Faktor dominan: tenure, jumlah komplain, cashback.  
- Recall tinggi lebih baik untuk strategi retensi.  

## Deployment
Model dapat di-deploy dengan **Streamlit**:  
```bash
streamlit run app.py
```

## Requirements
- Python 3.10+  
- pandas, numpy, scikit-learn, imbalanced-learn, xgboost, seaborn, matplotlib, streamlit  

## Next Step
- Interpretabilitas model (SHAP/feature importance).  
- Integrasi database real-time & CRM.  
