import joblib
import pandas as pd

# load model & kolom
model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

# sample awal (boleh sedikit dulu)
sample = pd.DataFrame(
    [{"Age": 30, "MonthlyIncome": 3000, "YearsAtCompany": 1, "OverTime_Yes": 1}]
)

# samakan kolom
sample = pd.get_dummies(sample)

# tambahkan kolom yang hilang
sample = sample.reindex(columns=columns, fill_value=0)

# prediksi
prediction = model.predict(sample)

print("Prediction:", prediction)

proba = model.predict_proba(sample)

print("Probability:", proba)
