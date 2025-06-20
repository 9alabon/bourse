from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Database Configuration (replace with your actual connection string)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Placeholder route
@app.route('/api/test')
def test_route():
    return jsonify({'message': 'Backend is working!'})

if __name__ == '__main__':
    app.run(debug=True)
