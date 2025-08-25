from flask import Flask, render_template, request
import pickle
import os

# Lấy đường dẫn tuyệt đối đến thư mục gốc (DECISIONTREE)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_PATH = os.path.join(BASE_DIR, "models", "mushroom_model.pkl")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# Load model đã train
with open(MODEL_PATH, "rb") as f:
    tree = pickle.load(f)

# Hàm dự đoán (copy từ predict_mushroom.py)
def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree
    feature = next(iter(tree))
    value = sample.get(feature, None)
    if value in tree[feature]:
        return predict(tree[feature][value], sample)
    else:
        return "Không xác định"

# Khởi tạo Flask app, chỉ định thư mục templates rõ ràng
app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        odor = request.form.get("odor")
        cap_color = request.form.get("cap_color")
        gill_color = request.form.get("gill_color")

        sample = {
            "odor": odor,
            "cap-color": cap_color,
            "gill-color": gill_color
        }

        prediction = predict(tree, sample)
        if prediction == "e":
            result = "🍄 Nấm ăn được (Edible)"
        elif prediction == "p":
            result = "☠️ Nấm độc (Poisonous)"
        else:
            result = "⚠️ Không xác định"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
