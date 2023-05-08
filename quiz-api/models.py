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

class PossibleAnswer(db.Model):
    __tablename__ = 'possibleAnswers'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))

    def __repr__(self):
        return f'<PossibleAnswer {self.text}>'

    def to_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'is_correct': self.is_correct
        }