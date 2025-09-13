import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("diabetes.csv")  # Make sure this CSV is in the same folder

# Drop 'Pregnancies' for a gender-neutral model
X = df.drop(["Outcome", "Pregnancies"], axis=1)
y = df["Outcome"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
with open("diabetes_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as diabetes_model.pkl")
