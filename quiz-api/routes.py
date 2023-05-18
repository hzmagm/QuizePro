import hashlib
import json
from flask import Blueprint, jsonify, request, session
from jwt_utils import build_token,decode_token
from models import PossibleAnswer, Question, Participant, db

questions_routes = Blueprint('questions_routes', __name__, url_prefix='/questions')

Admin_routes= Blueprint('Admin_routes', __name__, url_prefix='/admin')

participations_routes=Blueprint('participations_routes', __name__, url_prefix='/participations')


@questions_routes.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return {"size": 0, "scores": []}, 200

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

# GET questions by position
@questions_routes.route('',methods=['GET'])
def question_by_position():
    position = request.args.get('position')
    questions = Question.query.filter_by(position=position).all()
    if questions:
        return jsonify(Question.normalize_to_list(questions)),200
    else:
        return 'Question not found for the given position', 404

######## Participant EndPoints ########

# Add participant 
@participations_routes.route('/add', methods=['POST'])
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
@participations_routes.route('/all', methods=['GET'])
def get_all_participant() : 
    participants = Participant.query.all()
    if(participants):
        return jsonify([participant.to_dict() for participant in participants]), 200
    else :
        return 'There no particpants in the database !',404

# Get ordered participant by score 
@participations_routes.route('/all_ordered', methods=['GET'])
def get_all_participant_ordered() : 
    participants = Participant.query.order_by(Participant.score.desc()).all()
    if(participants):
        return jsonify([participant.to_dict() for participant in participants]), 200
    else :
        return 'There no particpants in the database !',404

# Get particpant by Id 
@participations_routes.route('/<int:particpant_id>', methods=['GET'])
def get_particpant_by_id(particpant_id):
    participant = Participant.query.get(particpant_id)
    if(participant):
        return jsonify(participant.to_dict()),200
    else:
        return 'Participant not found for the given Id', 404

# Update participant score
@participations_routes.route('/<int:particpant_id>', methods=['PUT'])
def update_participation_by_id(particpant_id):
    participant = Participant.query.get(particpant_id)
    data = request.json
    participant.score=data.get('score', participant.score)
    result=db.session.commit()
    if result is None :
        return f'Participant with Id {particpant_id} updated successfully', 200
    else :
        return f'Participant with Id {particpant_id} has not ben updated successfully', 500

######## Admin EndPoints ########

# Login
@Admin_routes.route('/login', methods=['POST'])
def Auth():
    payload = request.get_json()
    tried_pass = payload['password'].encode('UTF-8')
    hashed = hashlib.md5(tried_pass).digest()
    if hashed == b"\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@":
        token = build_token()
        value = {
            "token": token,
        }
        session['token'] = token
        return json.dumps(value)
    else:
        return 'Unauthorized', 401
# Logout 
@Admin_routes.route('/logout', methods=['POST'])
def logout():
    session.pop('token', None)
    return 'Logged out successfully'

# Update question
@Admin_routes.route('/questions/<int:question_id>', methods=['PUT'])
def update_question_by_id(question_id):
    token=decode_token(session.get('token'))
    if("quiz-app-admin"==token):
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
        result=db.session.commit()
        if result is None:
            return f'Question with ID {question_id} updated successfully', 200
        else :
            return f'Question with ID {question_id} has not been updated', 500
    else:
        return 'Unauthorized', 401

# Add a new question
@Admin_routes.route('/questions/', methods=['POST'])
def add_question():
    token=decode_token(session.get('token'))
    if("quiz-app-admin"==token):
        data = request.json
        question_text = data.get('text')
        question_title = data.get('title')
        question_image = data.get('image')
        question_position = data.get('position')
        possible_answers = data.get('possibleAnswers', [])

        new_question = Question(text=question_text, title=question_title, image=question_image, position=question_position)
        db.session.add(new_question)
        result_quest=db.session.commit()

        for answer in possible_answers:
            answer_text = answer.get('text')
            isCorrect = answer.get('isCorrect',False)
            new_answer = PossibleAnswer(text=answer_text, isCorrect=isCorrect, question_id=new_question.id)
            db.session.add(new_answer)

        result_ans=db.session.commit()
        if result_quest is None and result_ans is None :
            return f'Question with Id {new_question.id} has been added successfully', 200
        else :
            return f'Question with Id {new_question.id} has not been added', 500
    else:
        return 'Unauthorized', 401

# Delete the possible answers associated with the question by Id
@Admin_routes.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question_by_id(question_id):
    token=decode_token(session.get('token'))
    if("quiz-app-admin"==token):
        question = db.session.query(Question).filter(Question.id==question_id).first()
        for answer in question.answers:
            db.session.delete(answer)
        db.session.delete(question)
        result=db.session.commit()
        if result is None:
            return f'Question with Id {question_id} deleted successfully', 200
        else:
            return f'Question with Id {question_id} has not been deleted', 500
    else:
        return 'Unauthorized', 401
# Delete all the possible answers associated with the question
@Admin_routes.route('/questions/delete', methods=['DELETE'])
def delete_all_question():
    token=decode_token(session.get('token'))
    if("quiz-app-admin"==token):
        Question.query.delete()
        PossibleAnswer.query.delete()
        result=db.session.commit()
        if result is None:
            return 'Questions has been deleted succefully', 200
        else:
            return 'Questions has not been deleted', 500
    else:
        return 'Unauthorized', 401

# Delete participant score
@Admin_routes.route('/participations/all', methods=['DELETE'])
def delete_participations():
    token=decode_token(session.get('token'))
    if("quiz-app-admin"==token):
        Participant.query.delete()
        result=db.session.commit()
        if result is None :
            return '',204 
        else :
            return '', 500
    else:
        return 'Unauthorized', 401