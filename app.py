from flask import Flask, request, jsonify
from controllers.MongoController import user_service

app = Flask(__name__)

@app.route('/')
def main():
    return 'Oiem'

@app.route('/cadastro', methods=['POST'])
def create_user():
    data = request.get_json(force=True)
    user = user_service.create_user(data)
    return jsonify(user)

@app.route('/login', methods=['GET'])
def login():
    userF = request.get_json(force=True)
    
    return jsonify(user)

if __name__ == "__main__":
    app.run(port=8000, host='localhost', debug=True)
