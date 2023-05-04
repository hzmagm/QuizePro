import json
import sqlite3,os
import jwt,hashlib
from flask import Flask, jsonify, request,g
from flask_cors import CORS
from jwt_utils import build_token

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
CORS(app)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/questions/all', methods=['GET'])
def get_All_Questions():
    conn = sqlite3.connect('QuizePro.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM questions').fetchall()
    return jsonify(all_books)

@app.route('/questions/<id>', methods=['GET'])
def get_Questions_by_Id(id):
    conn = sqlite3.connect('QuizePro.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_quest = cur.execute('SELECT * FROM questions WHERE id='+id).fetchone()
    all_answ = cur.execute('SELECT text,isCorrect FROM possibleAnswers WHERE question_Id='+id).fetchall()
    
    for answer in all_answ:
        answer['isCorrect'] = bool(answer['isCorrect'])
        
    return jsonify({
        "text":all_quest["text"],
        "title":all_quest["title"],
        "image":all_quest["image"],
        "position":all_quest["position"],
        'possibleAnswers': all_answ})

@app.route('/questions')
def get_Questions_by_Position():
    position = request.args.get('position')
    conn = sqlite3.connect('QuizePro.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_quest = cur.execute('SELECT * FROM questions WHERE position=?', (position,)).fetchone()
    all_answ = cur.execute('SELECT text,isCorrect FROM possibleAnswers WHERE question_Id=?',(all_quest["id"],)).fetchall()
    conn.close()
    if all_quest:
        # Return a JSON response with the question details
        return jsonify({
            "text":all_quest["text"],
            "title":all_quest["title"],
            "image":all_quest["image"],
            "position":all_quest["position"],
            'possibleAnswers': all_answ})
    else:
        # Return a JSON response with an error message
        return jsonify({
            "error": "Question not found for the given position"
        })

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