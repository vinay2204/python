from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (or configure as needed)

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        data = request.get_json()
        print("Received data:", data)  # Process the data as needed
        return jsonify({'message': 'Data received successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)