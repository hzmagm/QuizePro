from models import Question, PossibleAnswer, db, Participant

def creat_dummy_data():
    
    question1 = Question(title='Dummy Question', position=1, text='Quelle est la couleur du cheval blanc d''Henry IV ?', image=None)
    possible_answer1 = PossibleAnswer(text='Noir', isCorrect=False, question=question1)
    possible_answer2 = PossibleAnswer(text='Gris', isCorrect=False, question=question1)
    possible_answer3 = PossibleAnswer(text='Blanc', isCorrect=True, question=question1)
    possible_answer4 = PossibleAnswer(text='La réponse D', isCorrect=False, question=question1)

    question2 = Question(title='What is the largest mammal in the world?', position=2, text='Select the correct answer for the following question:', image=None)
    possible_answer5 = PossibleAnswer(text='Blue Whale', isCorrect=True, question=question2)
    possible_answer6 = PossibleAnswer(text='Elephant', isCorrect=False, question=question2)
    possible_answer7 = PossibleAnswer(text='Giraffe', isCorrect=False, question=question2)

    question3 = Question(title='What is the name of the highest mountain in the world?', position=3, text='Select the correct answer for the following question:', image=None)
    possible_answer8 = PossibleAnswer(text='Mount Everest', isCorrect=True, question=question3)
    possible_answer9 = PossibleAnswer(text='K2', isCorrect=False, question=question3)
    possible_answer10 = PossibleAnswer(text='Kilimanjaro', isCorrect=False, question=question3)

    question4 = Question(title='Who invented the telephone?', position=4, text='Select the correct answer for the following question:', image=None)
    possible_answer11 = PossibleAnswer(text='Alexander Graham Bell', isCorrect=True, question=question4)
    possible_answer12 = PossibleAnswer(text='Thomas Edison', isCorrect=False, question=question4)
    possible_answer13 = PossibleAnswer(text='Nikola Tesla', isCorrect=False, question=question4)

    question5 = Question(title='What is the smallest country in the world by land area?', position=5, text='Select the correct answer for the following question:', image=None)
    possible_answer14 = PossibleAnswer(text='Vatican City', isCorrect=True, question=question5)
    possible_answer15 = PossibleAnswer(text='Monaco', isCorrect=False, question=question5)
    possible_answer16 = PossibleAnswer(text='Nauru', isCorrect=False, question=question5)
    
    participant1 = Participant(pseudoName='John', score=5)
    participant2 = Participant(pseudoName='Sarah', score=8)
    participant3 = Participant(pseudoName='David', score=12)
    participant4 = Participant(pseudoName='Emma', score=3)
    participant5 = Participant(pseudoName='Michael', score=7)
    participant6 = Participant(pseudoName='Oliver', score=15)
    participant7 = Participant(pseudoName='Sophie', score=9)
    participant8 = Participant(pseudoName='Adam', score=2)
    participant9 = Participant(pseudoName='Avery', score=6)
    participant10 = Participant(pseudoName='Grace', score=11)
    participant11 = Participant(pseudoName='Liam', score=7)
    participant12 = Participant(pseudoName='Ella', score=4)
    participant13 = Participant(pseudoName='Nathan', score=13)
    participant14 = Participant(pseudoName='Aiden', score=1)
    participant15 = Participant(pseudoName='Leah', score=8)
    participant16 = Participant(pseudoName='Jacob', score=10)
    participant17 = Participant(pseudoName='Chloe', score=6)
    participant18 = Participant(pseudoName='Ethan', score=14)
    participant19 = Participant(pseudoName='Mia', score=5)
    participant20 = Participant(pseudoName='Logan', score=12)
    participant21 = Participant(pseudoName='Emily', score=9)
    participant22 = Participant(pseudoName='Daniel', score=7)
    participant23 = Participant(pseudoName='Aria', score=3)
    participant24 = Participant(pseudoName='Lucas', score=11)
    
    
    db.session.add_all([question1, question2, question3, question4, question5,possible_answer1, possible_answer2, possible_answer3, possible_answer4,possible_answer5, possible_answer6, possible_answer7, possible_answer8, possible_answer9, possible_answer10, possible_answer11, possible_answer12, possible_answer13, possible_answer14, possible_answer15, possible_answer16, participant1, participant2, participant3, participant4, participant5, participant6, participant7, participant8, participant9, participant10, participant11, participant12, participant13, participant14, participant15, participant16, participant17, participant18, participant19, participant20, participant21, participant22, participant23, participant24])
    db.session.commit()