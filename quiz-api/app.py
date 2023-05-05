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

#Get all questions 
@app.route('/questions/all', methods=['GET'])
def get_All_Questions():
    conn = sqlite3.connect('QuizePro.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM questions').fetchall()
    return jsonify(all_books)

#Get question by Id
@app.route('/questions/<id>', methods=['GET'])
def get_Questions_by_Id(id):
    conn = sqlite3.connect('QuizePro.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_quest = cur.execute('SELECT * FROM questions WHERE id='+id).fetchone()
    all_answ = cur.execute('SELECT text,isCorrect FROM possibleAnswers WHERE question_Id='+id).fetchall()
    
    for answer in all_answ:
        answer['isCorrect'] = bool(answer['isCorrect'])
    if all_quest:     
        return jsonify({
            "text":all_quest["text"],
            "title":all_quest["title"],
            "image":all_quest["image"],
            "position":all_quest["position"],
            'possibleAnswers': all_answ})
    else:
        return 'Question not found for the given Id', 404
    
#Update question
@app.route('/questions/<id>', methods=['PUT'])
def update_question_by_id(id):
    conn = sqlite3.connect('QuizePro.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute('SELECT * FROM questions WHERE id=?', (id,))
    question = cur.fetchone()
    if not question:
        return 'Question not found for the given Id', 404

    data = request.json
    text = data.get('text', question['text'])
    title = data.get('title', question['title'])
    image = data.get('image', question['image'])
    position = data.get('position', question['position'])
    possible_answers = data.get('possibleAnswers', [])

    cur.execute('UPDATE questions SET text=?, title=?, image=?, position=? WHERE id=?',
                (text, title, image, position, id))
    conn.commit()

    cur.execute('DELETE FROM possibleAnswers WHERE question_Id=?', (id,))
    for answer in possible_answers:
        text = answer.get('text', '')
        is_correct = answer.get('isCorrect', False)
        cur.execute('INSERT INTO possibleAnswers (text, isCorrect, question_Id) VALUES (?, ?, ?)',
                    (text, is_correct, id))
    conn.commit()
    return f'Question with ID {id} updated successfully' , 204

#Create a new question
@app.route('/questions', methods=['POST'])
def create_question():
    data = request.get_json()

    text = data['text']
    title = data['title']
    image = data['image']
    position = data['position']
    
    conn = sqlite3.connect('QuizePro.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO questions (text, title, image, position) VALUES (?, ?, ?, ?)", (text, title, image, position))
    question_id = cur.lastrowid 
    
    possible_answers = data['possibleAnswers']
    for answer in possible_answers:
        answer_text = answer['text']
        is_correct = answer['isCorrect']
        cur.execute("INSERT INTO possibleAnswers (question_Id, text, isCorrect) VALUES (?, ?, ?)", (question_id, answer_text, is_correct))
    
    conn.commit()
    conn.close()
    created_question = {'id': question_id, 'text': text, 'title': title, 'image': image, 'position': position, 'possibleAnswers': possible_answers}

    return jsonify(created_question), 200

#Get questions by position
@app.route('/questions')
def get_Questions_by_Position():
    position = request.args.get('position')
    conn = sqlite3.connect('QuizePro.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_quest = cur.execute('SELECT * FROM questions WHERE position=?', (position,)).fetchone()
    if all_quest:
        all_answ = cur.execute('SELECT text,isCorrect FROM possibleAnswers WHERE question_Id=?',(all_quest["id"],)).fetchall()
        conn.close()
        return jsonify({
            "text":all_quest["text"],
            "title":all_quest["title"],
            "image":all_quest["image"],
            "position":all_quest["position"],
            'possibleAnswers': all_answ})
    else:
        return "Question not found for the given position", 404
            
#TODO : Login
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