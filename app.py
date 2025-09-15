import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("bestmodel_churn.sav")

st.title("📊 Prediksi Customer Churn")

st.write("Masukkan data pelanggan untuk memprediksi apakah akan churn atau tidak.")

# Form input sesuai fitur saat training
Tenure = st.number_input("Tenure (lama berlangganan, bulan)", min_value=0, max_value=100, value=12)
WarehouseToHome = st.number_input("Jarak Warehouse ke Rumah (km)", min_value=0, max_value=100, value=10)
NumberOfDeviceRegistered = st.number_input("Jumlah Device Terdaftar", min_value=1, max_value=10, value=2)
PreferedOrderCat = st.selectbox("Kategori Order Favorit", 
                                ["Laptop & Accessory", "Mobile", "Fashion", "Grocery", "Others"])
SatisfactionScore = st.slider("Skor Kepuasan", 1, 5, 3)
MaritalStatus = st.selectbox("Status Pernikahan", ["Single", "Married", "Divorced"])
NumberOfAddress = st.number_input("Jumlah Alamat Tersimpan", min_value=1, max_value=10, value=1)
Complain = st.selectbox("Pernah Komplain?", [0, 1])
DaySinceLastOrder = st.number_input("Hari sejak order terakhir", min_value=0, max_value=1000, value=10)
CashbackAmount = st.number_input("Jumlah Cashback", min_value=0.0, max_value=10000.0, value=200.0)

# Susun input sesuai kolom training
feature_names = [
    "Tenure", "WarehouseToHome", "NumberOfDeviceRegistered", 
    "PreferedOrderCat", "SatisfactionScore", "MaritalStatus", 
    "NumberOfAddress", "Complain", "DaySinceLastOrder", "CashbackAmount"
]

user_input = {
    "Tenure": Tenure,
    "WarehouseToHome": WarehouseToHome,
    "NumberOfDeviceRegistered": NumberOfDeviceRegistered,
    "PreferedOrderCat": PreferedOrderCat,
    "SatisfactionScore": SatisfactionScore,
    "MaritalStatus": MaritalStatus,
    "NumberOfAddress": NumberOfAddress,
    "Complain": Complain,
    "DaySinceLastOrder": DaySinceLastOrder,
    "CashbackAmount": CashbackAmount
}

input_data = pd.DataFrame([user_input], columns=feature_names)

# Prediksi
if st.button("Prediksi Churn"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Customer diprediksi akan **CHURN**.")
    else:
        st.success("✅ Customer diprediksi **TIDAK churn**.")