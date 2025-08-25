import pandas as pd
import numpy as np
import pickle
import os
import pandas as pd
from sklearn.model_selection import train_test_split

# ------------------------
# ID3 Implementation
# ------------------------

def entropy(y):
    values, counts = np.unique(y, return_counts=True)
    probs = counts / counts.sum()
    return -np.sum(probs * np.log2(probs))

def information_gain(X, y, feature):
    values, counts = np.unique(X[feature], return_counts=True)
    weighted_entropy = np.sum([
        (counts[i] / np.sum(counts)) * entropy(y[X[feature] == values[i]])
        for i in range(len(values))
    ])
    return entropy(y) - weighted_entropy

def id3(X, y, features):
    if len(np.unique(y)) == 1:
        return y.iloc[0]
    if len(features) == 0:
        return y.mode()[0]

    gains = [information_gain(X, y, f) for f in features]
    best_feature = features[np.argmax(gains)]

    tree = {best_feature: {}}
    for value in np.unique(X[best_feature]):
        sub_X = X[X[best_feature] == value]
        sub_y = y[X[best_feature] == value]
        remaining_features = [f for f in features if f != best_feature]
        tree[best_feature][value] = id3(sub_X, sub_y, remaining_features)
    return tree

# ------------------------
# Hàm dự đoán
# ------------------------
def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    value = sample.get(feature, None)
    if value in tree[feature]:
        return predict(tree[feature][value], sample)
    else:
        # nếu giá trị không có trong cây thì fallback -> dự đoán mode "e"
        return "e"

# ------------------------
# Load Mushroom dataset
# ------------------------
#data = pd.read_csv("mushrooms.csv")
# Lấy đường dẫn tuyệt đối tới thư mục gốc của project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  

# Nối đường dẫn tới thư mục data
data_path = os.path.join(BASE_DIR, "data", "mushrooms.csv")

# Đọc file
data = pd.read_csv(data_path)

X = data.drop("class", axis=1)
y = data["class"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Huấn luyện mô hình
features = list(X_train.columns)
tree = id3(X_train, y_train, features)

# ------------------------
# Đánh giá mô hình
# ------------------------
from sklearn.metrics import confusion_matrix, classification_report

y_pred = [predict(tree, X_test.iloc[i].to_dict()) for i in range(len(X_test))]

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("📊 Confusion Matrix:")
print(cm)

# Classification Report (Precision, Recall, F1-score)
print("\n📑 Classification Report:")
print(classification_report(y_test, y_pred, digits=4))

# Accuracy tổng thể
accuracy = np.mean(y_pred == y_test)
print(f"🎯 Độ chính xác trên tập test: {accuracy:.4f}")

# ------------------------
# Lưu mô hình đã huấn luyện
# ------------------------
# luôn chắc chắn file lưu trong thư mục models nằm trong DecisionTree
base_dir = os.path.dirname(os.path.dirname(__file__))  # thư mục DecisionTree
model_dir = os.path.join(base_dir, "models")
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, "mushroom_model.pkl")
with open(model_path, "wb") as f:
    pickle.dump(tree, f)

print(f"✅ Mô hình đã huấn luyện và lưu tại {model_path}")
