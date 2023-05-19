from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(80))

    answers = db.relationship('PossibleAnswer', backref='question')

    def __repr__(self):
        return f'<Question {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'position': self.position,
            'text': self.text,
            'image': self.image,
            'answers': [answer.to_dict() for answer in self.answers]
        }
        
    def to_dict_list(objects):
        return [obj.to_dict() for obj in objects]
    
    def normalize_to_list(list):
        data=[]
        for question in list :
            data.append(
                {
                'id': question.id,
                'title': question.title,
                'position': question.position,
                'text': question.text,
                'image': question.image,
                'answers': [answer.to_dict() for answer in question.answers]
                })
        return data
        
    
class PossibleAnswer(db.Model):
    __tablename__ = 'possibleAnswers'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=False)
    isCorrect = db.Column(db.Boolean, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    
    def __repr__(self):
        return f'<PossibleAnswer {self.text}>'

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'isCorrect': self.isCorrect
        }

class Participant(db.Model):
    __tablename__ = 'participant'
    
    id = db.Column(db.Integer, primary_key=True)
    pseudoName = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Participant {self.text}>'

    def to_dict(self):
        return {
            'id': self.id,
            'pseudoName': self.pseudoName,
            'score': self.score
        }