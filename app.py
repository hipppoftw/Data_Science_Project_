import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier



data = pd.read_csv("data.csv")
df = pd.DataFrame(data)

#cut down the columns to get just the important ones
subset = df[['tenure','Contract', 'MonthlyCharges', 'Churn']]
print(subset.head(20))


X_raw = subset.drop("Churn", axis = 1)
#Define features
features = pd.get_dummies(X_raw, columns = ['Contract'])
print(features.head(20))

#transform Yes/No into Numeric
target = subset['Churn'].map({'Yes': 1, "No": 0})

#Concatenate the 2 subsets to get the targeted data
processed_data = pd.concat([features,target], axis = 1)
print(processed_data.head())

# 1. Define X (Features/Input) and y (Target/Output)
X = features
y = target

#2. Split the data into training and testing
# test_size=0.2 means 20% of data goes to testing, 80% to training.
# random_state=42 ensures you get the exact same random split every time you run this.
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)



model = LogisticRegression(random_state=0)
model.fit(X_train,y_train)
prediction = accuracy_score(y_test, model.predict(X_test))
print(prediction)

# Coefficients and Odds Ratios
coefficients = model.coef_[0]
odds_ratios = np.exp(coefficients)

# Display feature importance using coefficients and odds ratios
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': coefficients,
    'Odds Ratio': odds_ratios
})
print("\nFeature Importance (Coefficient and Odds Ratio):")
print(feature_importance.sort_values(by='Coefficient', ascending=False))


# Random Forest to test multiple options
model_forest = RandomForestClassifier(n_estimators=100, random_state=42)
model_forest.fit(X_train,y_train)

y_pred = model_forest.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))