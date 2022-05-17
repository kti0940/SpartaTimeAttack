import json
import hashlib

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

    pw_hash = hashlib.sha256(data.get('password').encode('utf-8')).hexdigest()

    doc = {
        'email': data.get('email'),
        'password': pw_hash
    }

    print(doc)
    db.turtleuser.insert_one(doc)
    print(doc)

    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
