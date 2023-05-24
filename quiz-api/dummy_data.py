from models import Question, PossibleAnswer, db, Participant

def creat_dummy_data():
    
    question1 = Question(title='What is the color of Henry IV''s white horse?', position=1, text='Select the correct answer for the following question:', image=None)
    possible_answer1 = PossibleAnswer(text='Black', isCorrect=False, question=question1)
    possible_answer2 = PossibleAnswer(text='Grey', isCorrect=False, question=question1)
    possible_answer3 = PossibleAnswer(text='White', isCorrect=True, question=question1)

    question2 = Question(title='What is the largest mammal in the world?', position=2, text='Select the correct answer for the following question:', image=None)
    possible_answer6 = PossibleAnswer(text='Elephant', isCorrect=False, question=question2)
    possible_answer5 = PossibleAnswer(text='Blue Whale', isCorrect=True, question=question2)
    possible_answer7 = PossibleAnswer(text='Giraffe', isCorrect=False, question=question2)

    question3 = Question(title='What is the name of the highest mountain in the world?', position=3, text='Select the correct answer for the following question:', image=None)
    possible_answer8 = PossibleAnswer(text='Mount Everest', isCorrect=True, question=question3)
    possible_answer9 = PossibleAnswer(text='K2', isCorrect=False, question=question3)
    possible_answer10 = PossibleAnswer(text='Kilimanjaro', isCorrect=False, question=question3)

    question4 = Question(title='Who invented the telephone?', position=4, text='Select the correct answer for the following question:', image=None)
    possible_answer12 = PossibleAnswer(text='Thomas Edison', isCorrect=False, question=question4)
    possible_answer13 = PossibleAnswer(text='Nikola Tesla', isCorrect=False, question=question4)
    possible_answer11 = PossibleAnswer(text='Alexander Graham Bell', isCorrect=True, question=question4)

    question5 = Question(title='What is the smallest country in the world by land area?', position=5, text='Select the correct answer for the following question:', image=None)
    possible_answer16 = PossibleAnswer(text='Nauru', isCorrect=False, question=question5)
    possible_answer14 = PossibleAnswer(text='Vatican City', isCorrect=True, question=question5)
    possible_answer15 = PossibleAnswer(text='Monaco', isCorrect=False, question=question5)
    
    
    question6 = Question(title="Who painted the Mona Lisa?", position=6, text="Select the correct answer for the following question:", image=None)
    possible_answer17 = PossibleAnswer(text="Leonardo da Vinci", isCorrect=True, question=question6)
    possible_answer18 = PossibleAnswer(text="Vincent van Gogh", isCorrect=False, question=question6)
    possible_answer19 = PossibleAnswer(text="Pablo Picasso", isCorrect=False, question=question6)

    question7 = Question(title="What is the capital city of France?", position=7, text="Select the correct answer for the following question:", image=None)
    possible_answer21 = PossibleAnswer(text="London", isCorrect=False, question=question7)
    possible_answer20 = PossibleAnswer(text="Paris", isCorrect=True, question=question7)
    possible_answer22 = PossibleAnswer(text="Rome", isCorrect=False, question=question7)

    question8 = Question(title="What is the chemical symbol for gold?", position=8, text="Select the correct answer for the following question:", image=None)
    possible_answer23 = PossibleAnswer(text="Au", isCorrect=True, question=question8)
    possible_answer24 = PossibleAnswer(text="Ag", isCorrect=False, question=question8)
    possible_answer25 = PossibleAnswer(text="Fe", isCorrect=False, question=question8)

    question9 = Question(title="Who wrote the play 'Romeo and Juliet'?", position=9, text="Select the correct answer for the following question:", image=None)
    possible_answer26 = PossibleAnswer(text="William Shakespeare", isCorrect=True, question=question9)
    possible_answer27 = PossibleAnswer(text="Charles Dickens", isCorrect=False, question=question9)
    possible_answer28 = PossibleAnswer(text="Jane Austen", isCorrect=False, question=question9)

    question10 = Question(title="What is the largest ocean in the world?", position=10, text="Select the correct answer for the following question:", image=None)
    possible_answer30 = PossibleAnswer(text="Atlantic Ocean", isCorrect=False, question=question10)
    possible_answer29 = PossibleAnswer(text="Pacific Ocean", isCorrect=True, question=question10)
    possible_answer31 = PossibleAnswer(text="Indian Ocean", isCorrect=False, question=question10)
    
    participant1 = Participant(pseudoName='John', score=5)
    participant2 = Participant(pseudoName='Sarah', score=8)
    participant4 = Participant(pseudoName='Emma', score=3)
    participant5 = Participant(pseudoName='Michael', score=7)
    participant6 = Participant(pseudoName='Oliver', score=1)
    participant7 = Participant(pseudoName='Sophie', score=9)
    participant8 = Participant(pseudoName='Adam', score=2)
    participant9 = Participant(pseudoName='Avery', score=6)
    participant11 = Participant(pseudoName='Liam', score=7)
    participant12 = Participant(pseudoName='Ella', score=4)
    participant14 = Participant(pseudoName='Aiden', score=1)
    participant15 = Participant(pseudoName='Leah', score=8)
    participant17 = Participant(pseudoName='Chloe', score=6)
    participant19 = Participant(pseudoName='Mia', score=5)
    participant21 = Participant(pseudoName='Emily', score=9)
    participant22 = Participant(pseudoName='Daniel', score=7)
    participant23 = Participant(pseudoName='Aria', score=3)
    
    db.session.add_all([question1, question2, question3, question4, question5,question6,question7,question8,question9,question10,possible_answer1, possible_answer2, possible_answer3,possible_answer5, possible_answer6, possible_answer7, possible_answer8, possible_answer9, possible_answer10, possible_answer11, possible_answer12, possible_answer13, possible_answer14, possible_answer15, possible_answer16,possible_answer17,possible_answer18,possible_answer19,possible_answer20,possible_answer21,possible_answer22,possible_answer23,possible_answer24,possible_answer25,possible_answer26,possible_answer27,possible_answer28,possible_answer29,possible_answer30,possible_answer31, participant1, participant2, participant4, participant5, participant6, participant7, participant8, participant9, participant11, participant12, participant14, participant15, participant17, participant19, participant21, participant22, participant23])
    db.session.commit()