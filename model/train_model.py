import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Example dataset structure
# url_length,dot_count,has_https,has_at,has_dash,ip_length,label

data = pd.read_csv("dataset/malicious_urls.csv")

X = data.drop("label", axis=1)
y = data["label"]

model = RandomForestClassifier(n_estimators=100)

model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model saved successfully")