from flask import Blueprint, jsonify, request
from models import Question,db
questions_routes = Blueprint('questions_routes', __name__, url_prefix='/questions')

# Get all questions
@questions_routes.route('/', methods=['GET'])
def get_all_questions():
    Qst=Question()
    questions = Question.query.all()
    if(questions):
        return jsonify([question.to_dict() for question in questions])
    else :
        return 404
    
# Get question by Id
@questions_routes.route('/<int:question_id>')
def question_by_id(question_id):
    question = Question.query.get(question_id)
    if(question):
        return jsonify(question.to_dict()),200
    else:
        return 'Question not found for the given Id', 404

# TODO : Update question
@questions_routes.route('/<int:question_id>', methods=['PUT'])
def update_question_by_id(question_id):
    question = Question.query.get(question_id)
    data = request.json
    question.text = data.get('text', question.text)
    question.title = data.get('title', question.title)
    question.image = data.get('image', question.image)
    question.position = data.get('position', question.position)
    question.answers = data.get('possibleAnswers', [])
    db.session.commit()
    return f'Question with ID {question_id} updated successfully', 204
