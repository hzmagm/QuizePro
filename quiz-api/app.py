import json
import sqlite3,os
import jwt,hashlib
from flask import Flask, jsonify, request,g
from flask_cors import CORS
from jwt_utils import build_token

app = Flask(__name__)
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

@app.route('/questions', methods=['GET'])
def api_all():
    conn = sqlite3.connect('QuizePro.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM questions').fetchall()
    return jsonify(all_books)

@app.route('/questions/<id>', methods=['GET'])
def api_id(id):
    conn = sqlite3.connect('QuizePro.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM questions JOIN possibleAnswers WHERE questions.id=possibleAnswers.question_Id and questions.id='+id).fetchall()
    return jsonify(all_books)

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

#@app.route('/questions/<int:question_id>', methods=['GET'])
#def get_question(question_id):
#    question = Question.get_question_by_id(question_id)
#    possible_answers = []
#    for answer in question.possible_answers:
 #       possible_answers.append({
  #          'id': answer.id,
   #         'text': answer.text,
    #        'is_correct': answer.is_correct
     #   })
    #return jsonify({
     #   'id': question.id,
      #  'title': question.title,
       # 'position': question.position,
       # 'text': question.text,
       # 'image': question.image,
       # 'possible_answers': possible_answers
    #})

#@app.route('/questions/<int:question_id>', methods=['GET'])
#def getQuestById(question_id):
#    question = query_db('SELECT * from questions join possibleAnswers where possibleAnswers.question_Id==?',
#               [question_id], one=True)
#   print('connected')
#    if question is None:
#        return jsonify({'error': 'Question not found'}), 404
#    return jsonify(question)

if __name__ == "__main__":
    app.run()