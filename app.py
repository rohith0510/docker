
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    op = data["operation"]

    if op == "add":
        result = num1 + num2
    elif op == "sub":
        result = num1 - num2
    elif op == "mul":
        result = num1 * num2
    elif op == "div":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        result = 0

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
