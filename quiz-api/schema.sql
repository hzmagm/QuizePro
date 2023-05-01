

DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS possibleAnswers;

CREATE TABLE questions (
	id	INTEGER PRIMARY KEY AUTOINCREMENT,
	title 	TEXT,
	position	INTEGER,
	text	TEXT,
	image	BLOB,
);

CREATE TABLE possibleAnswers (
	id	INTEGER PRIMARY KEY AUTOINCREMENT,
	text 	TEXT,
	is_Correct 	INTEGER,
	question_Id	INTEGER,
	FOREIGN KEY(question_Id) REFERENCES questions(id)
);

INSERT INTO questions (title, position, text, image) VALUES ('What is the capital of France?', 1, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Paris', 1, 1);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('London', 0, 1);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('New York', 0, 1);

INSERT INTO questions (title, position, text, image) VALUES ('What is the largest mammal in the world?', 2, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Blue Whale', 1, 2);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Elephant', 0, 2);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Giraffe', 0, 2);

INSERT INTO questions (title, position, text, image) VALUES ('What is the name of the highest mountain in the world?', 3, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Mount Everest', 1, 3);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('K2', 0, 3);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Kilimanjaro', 0, 3);

INSERT INTO questions (title, position, text, image) VALUES ('Who invented the telephone?', 4, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Alexander Graham Bell', 1, 4);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Thomas Edison', 0, 4);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Nikola Tesla', 0, 4);

INSERT INTO questions (title, position, text, image) VALUES ('What is the smallest country in the world by land area?', 5, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Vatican City', 1, 5);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Monaco', 0, 5);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Nauru', 0, 5);

INSERT INTO questions (title, position, text, image) VALUES ('What is the chemical symbol for gold?', 6, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Au', 1, 6);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Ag', 0, 6);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Pt', 0, 6);

INSERT INTO questions (title, position, text, image) VALUES ('Which planet in our solar system is known as the "Red Planet"?', 7, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Mars', 1, 7);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Jupiter', 0, 7);
INSERT INTO possibleAnswers (text, is_Correct, question_Id) VALUES ('Venus', 0, 7);