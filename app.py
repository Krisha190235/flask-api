from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello from Cloud-Native API!",
        "status": "running",
        "version": "1.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/items')
def items():
    return jsonify({
        "items": [
            {"id": 1, "name": "Item One"},
            {"id": 2, "name": "Item Two"},
            {"id": 3, "name": "Item Three"}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
