DROP TABLE IF EXISTS questions;
DROP TABLE IF EXISTS possibleAnswers;

CREATE TABLE questions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT,
    position    INTEGER,
    text        TEXT,
    image       BLOB
);

CREATE TABLE possibleAnswers (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    text        TEXT,
    is_correct  TEXT,
    question_id INTEGER,
    FOREIGN KEY(question_id) REFERENCES questions(id)
);

INSERT INTO questions (title, position, text, image) VALUES ('Dummy Question', 1, 'Quelle est la couleur du cheval blanc d''Henry IV ?', NULL);

INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Noir', 'false', 1);
INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Gris', 'false', 1);
INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Blanc', 'true', 1);
INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('La réponse D', 'false', 1);

INSERT INTO questions (title, position, text, image) VALUES ('What is the largest mammal in the world?', 2, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Blue Whale', 'true', 2);
INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Elephant', 'false', 2);
INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Giraffe', 'false', 2);

INSERT INTO questions (title, position, text, image) VALUES ('What is the name of the highest mountain in the world?', 3, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Mount Everest', 'true', 3);
INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('K2', 'false', 3);
INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Kilimanjaro', 'false', 3);

INSERT INTO questions (title, position, text, image) VALUES ('Who invented the telephone?', 4, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Alexander Graham Bell', 'true', 4);
INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Thomas Edison', 'false', 4);
INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Nikola Tesla', 'false', 4);

INSERT INTO questions (title, position, text, image) VALUES ('What is the smallest country in the world by land area?', 5, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Vatican City', 'true', 5);
INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Monaco', 'false', 5);
INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Nauru', 'false', 5);

INSERT INTO questions (title, position, text, image) VALUES ('What is the chemical symbol for gold?', 6, 'Select the correct answer for the following question:', NULL);

INSERT INTO possibleAnswers (text, is_correct, question_id) VALUES ('Au', 'true