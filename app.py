from dataclasses import dataclass
import json
import hashlib
import jwt

from flask import Flask, jsonify, request  # 플라스크 서버 사용 필요한 기능들 임포트
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)  # Flask 실행?
cors = CORS(app, resources={r"*": {"origins": "*"}})

client = MongoClient('localhost', 27017)
db = client.turtlegram


@app.route("/")  # url 경로 지정
def hello_world():  # hello_world 로 함수 지정
    return jsonify({'message': 'success'})  # 결과값은 제이슨 형식으로 키:벨류를 돌려줌


@app.route("/signup", methods=["POST"])
def sign_up():
    data = json.loads(request.data)

    email = data.get('email')
    password = data.get('password')

    print(email, password)

    pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    doc = {
        'email': email,
        'password': pw_hash
    }

    db.turtleuser.insert_one(doc)
    print(doc)

    return jsonify({'status': 'success'})


@app.route("/login", methods=["POST"])
def login():
    print(request)
    data = json.loads(request.data)
    print(data)

    return jsonify({'status': 'success'})

    email = data.get("email")
    password = data.get("password")
    pw_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    print(pw_hash)

    result = db.users.find_one({
        'email': email,
        'password': pw_hash
    })

    print(result)

    if result is None:
        return jsonify({"message": "아이디나 비밀번호가 올바르지 않습니다"}), 401

    payload = {
        'id': str(result["_id"]),
        'exp': datetime.utcnow() + timedelta(second=60 * 60 * 24)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    print(token)

    return jsonify({"message": "success", "token": token})


@app.route("/getuserinfo", methods=["GET"])
def get_user_info():
    token = request.headers.get("Autorization")
    print(token)

    return jsonify({"message": "success"})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
