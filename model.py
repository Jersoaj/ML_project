import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("laptop_prices.csv")
print(df.columns)

# Selecting features and target
X = df[['RAM (GB)', 'Screen Size (inch)', 'Battery Life (hours)']]
y = df['Price']

# Splitting data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open("rf_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
