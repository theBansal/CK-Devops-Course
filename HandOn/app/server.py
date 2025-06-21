from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, this is a Dockerized Flask App!"

@app.route('/config')
def config():
    with open(os.environ.get('CONFIG_PATH', './app/config.json')) as f:
        config = json.load(f)
    return jsonify(config)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('APP_PORT', 5000)))
