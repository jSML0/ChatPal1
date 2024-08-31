from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print(data)  # Debugging line
    return jsonify({'received_data': data})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
