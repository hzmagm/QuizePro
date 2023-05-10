import hashlib
import json
from flask import Blueprint, jsonify, request
from jwt_utils import build_token

from models import PossibleAnswer, Question, Participant, db

questions_routes = Blueprint('questions_routes', __name__, url_prefix='/questions')

Admin_routes= Blueprint('Admin_routes', __name__, url_prefix='/admin')

participant_routes=Blueprint('participant_routes', __name__, url_prefix='/participant')

# Get all questions
@questions_routes.route('/', methods=['GET'])
def get_all_questions():
    questions = Question.query.all()
    if(questions):
        return jsonify([question.to_dict() for question in questions])
    else :
        return 'There no questions in the database !',404
    
# GET question by Id
@questions_routes.route('/<int:question_id>')
def question_by_id(question_id):
    question = Question.query.get(question_id)
    if(question):
        return jsonify(question.to_dict()),200
    else:
        return 'Question not found for the given Id', 404

# Update question
@questions_routes.route('/<int:question_id>', methods=['PUT'])
def update_question_by_id(question_id):
    question = Question.query.get(question_id)
    data = request.json
    question.text = data.get('text', question.text)
    question.title = data.get('title', question.title)
    question.image = data.get('image', question.image)
    question.position = data.get('position', question.position)
    question.answers.clear()
    for answer in question.answers:
        db.session.delete(answer)
    for answer_text in data.get('possibleAnswers', []):
        answer = PossibleAnswer(text=answer_text.get('text'), isCorrect=answer_text.get('isCorrect', False),question_id=question.id)
        db.session.add(answer)
    db.session.commit()
    return f'Question with ID {question_id} updated successfully', 204

# GET questions by position
@questions_routes.route('')
def question_by_position():
    position = request.args.get('position')
    questions = Question.query.filter_by(position=position).all()
    if questions:
        return jsonify(Question.normalize_to_list(questions)),200
    else:
        return 'Question not found for the given position', 404
    
# Delete all the possible answers associated with the question by Id
# TODO : delete the possible answers too 
@questions_routes.route('/<int:question_id>', methods=['DELETE'])
def delete_question_by_id(question_id):
    question = db.session.query(Question).filter(Question.id==question_id).first()
    db.session.delete(question)
    db.session.commit()
    return f'Question with Id {question_id} deleted successfully', 204

# Delete all the possible answers associated with the question
@questions_routes.route('/', methods=['DELETE'])
def delete_all_question():
    Question.query.delete()
    PossibleAnswer.query.delete()
    db.session.commit()
    return 'Questions has been deleted succefully', 204

# Add a new question
@questions_routes.route('/', methods=['POST'])
def add_question():
    data = request.json
    question_text = data.get('text')
    question_title = data.get('title')
    question_image = data.get('image')
    question_position = data.get('position')
    possible_answers = data.get('possibleAnswers', [])

    new_question = Question(text=question_text, title=question_title, image=question_image, position=question_position)
    db.session.add(new_question)
    db.session.commit()

    for answer in possible_answers:
        answer_text = answer.get('text')
        isCorrect = answer.get('isCorrect',False)
        new_answer = PossibleAnswer(text=answer_text, isCorrect=isCorrect, question_id=new_question.id)
        db.session.add(new_answer)

    db.session.commit()

    return f'Question with ID {new_question.id} added successfully', 200

# Add participant 
@participant_routes.route('/add', methods=['POST'])
def add_participant() : 
    data = request.json
    participant = Participant(pseudoName=data.get('pseudoName'),score=0)
    db.session.add(participant)
    db.session.commit()
    if participant : 
        return jsonify(participant.to_dict()), 200
    else :
        return 'The participant has not been created ! ', 500

# Get all paritipants 
@participant_routes.route('/all', methods=['GET'])
def get_all_participant() : 
    participants = Participant.query.all()
    if(participants):
        return jsonify([participant.to_dict() for participant in participants]), 200
    else :
        return 'There no particpants in the database !',404

#Get order participant by score 
@participant_routes.route('/all', methods=['GET'])
def get_all_participant() : 
    participants = Participant.query.order_by(Participant.score).all()
    if(participants):
        return jsonify([participant.to_dict() for participant in participants]), 200
    else :
        return 'There no particpants in the database !',404

# TODO : Login --> we should modify it in order to handle the username as well as the password
@Admin_routes.route('/login', methods=['POST'])
def Auth():
    payload = request.get_json()
    tried_pass = payload['password'].encode('UTF-8')
    hashed = hashlib.md5(tried_pass).digest()
    if hashed == b"\t\x8fk\xcdF!\xd3s\xca\xdeN\x83&'\xb4\xf6":
        token = build_token()
        value = {
            "token": token,
        }
        return json.dumps(value)
    else:
        return 'Unauthorized', 401

