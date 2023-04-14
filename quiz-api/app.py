import json
import jwt,hashlib
from flask import Flask, request
from flask_cors import CORS

from jwt_utils import build_token

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/login', methods=['POST'])
def Auth():
    payload = request.get_json()
    tried_pass=payload['password'].encode('UTF-8')
    hashed=hashlib.md5(tried_pass).digest()
    if hashed==b"\t\x8fk\xcdF!\xd3s\xca\xdeN\x83&'\xb4\xf6":
        token=build_token()
        value = {
        "token": token,
        }
        return json.dumps(value)
    else:
        return 'Unauthorized', 401


if __name__ == "__main__":
    app.run()