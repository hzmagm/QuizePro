from models import Question, PossibleAnswer,db

def creat_dummy_data():
    question1 = Question(title='Dummy Question', position=1, text='Quelle est la couleur du cheval blanc d''Henry IV ?', image=None)
    possible_answer1 = PossibleAnswer(text='Noir', is_correct=False, question=question1)
    possible_answer2 = PossibleAnswer(text='Gris', is_correct=False, question=question1)
    possible_answer3 = PossibleAnswer(text='Blanc', is_correct=True, question=question1)
    possible_answer4 = PossibleAnswer(text='La réponse D', is_correct=False, question=question1)

    question2 = Question(title='What is the largest mammal in the world?', position=2, text='Select the correct answer for the following question:', image=None)
    possible_answer5 = PossibleAnswer(text='Blue Whale', is_correct=True, question=question2)
    possible_answer6 = PossibleAnswer(text='Elephant', is_correct=False, question=question2)
    possible_answer7 = PossibleAnswer(text='Giraffe', is_correct=False, question=question2)

    question3 = Question(title='What is the name of the highest mountain in the world?', position=3, text='Select the correct answer for the following question:', image=None)
    possible_answer8 = PossibleAnswer(text='Mount Everest', is_correct=True, question=question3)
    possible_answer9 = PossibleAnswer(text='K2', is_correct=False, question=question3)
    possible_answer10 = PossibleAnswer(text='Kilimanjaro', is_correct=False, question=question3)

    question4 = Question(title='Who invented the telephone?', position=4, text='Select the correct answer for the following question:', image=None)
    possible_answer11 = PossibleAnswer(text='Alexander Graham Bell', is_correct=True, question=question4)
    possible_answer12 = PossibleAnswer(text='Thomas Edison', is_correct=False, question=question4)
    possible_answer13 = PossibleAnswer(text='Nikola Tesla', is_correct=False, question=question4)

    question5 = Question(title='What is the smallest country in the world by land area?', position=5, text='Select the correct answer for the following question:', image=None)
    possible_answer14 = PossibleAnswer(text='Vatican City', is_correct=True, question=question5)
    possible_answer15 = PossibleAnswer(text='Monaco', is_correct=False, question=question5)
    possible_answer16 = PossibleAnswer(text='Nauru', is_correct=False, question=question5)
    
    db.session.add_all([question1, question2, question3, question4, question5,    possible_answer1, possible_answer2, possible_answer3, possible_answer4,    possible_answer5, possible_answer6, possible_answer7, possible_answer8,    possible_answer9, possible_answer10, possible_answer11, possible_answer12,    possible_answer13, possible_answer14, possible_answer15, possible_answer16])
    db.session.commit()