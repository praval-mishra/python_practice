# ==================== LOGISTIC REGRESSION USING SKLEARN ====================

# Step 1: Import all necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris          # Example dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 2: Load the dataset
iris = load_iris()
X = iris.data      # Features (input) → 4 columns
y = iris.target    # Target labels (0, 1, 2)

# Optional: If using your own CSV file
# df = pd.read_csv('your_file.csv')
# X = df.iloc[:, :-1]   # all columns except last
# y = df.iloc[:, -1]    # last column is target

# Step 3: Split data into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.3,      # 30% test, 70% train
    random_state=42     # for reproducibility
)

# Step 4: Create the Logistic Regression model
model = LogisticRegression(
    max_iter=200,       # Increase if it doesn't converge
    solver='lbfgs',     # default and good for small datasets
    #multi_class='auto'  # handles multi-class automatically
)

# Step 5: Train the model (fit)
model.fit(X_train, y_train)

# Step 6: Make predictions on test data
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))