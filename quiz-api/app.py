import json
import sqlite3,os
import jwt,hashlib
from flask import Flask, jsonify, request,g
from flask_cors import CORS
from jwt_utils import build_token


app = Flask(__name__)
CORS(app)

DATABASE = 'D:/quiz-app/quiz-api/QuizePro.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

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
    
@app.route('/questions/<int:question_id>', methods=['GET'])
def getQuestById(question_id):
    question = query_db('SELECT * from questions join possibleAnswers where possibleAnswers.question_Id==?',
                [question_id], one=True)
    print('connected')
    if question is None:
        return jsonify({'error': 'Question not found'}), 404
    return jsonify(question)

if __name__ == "__main__":
    app.run()