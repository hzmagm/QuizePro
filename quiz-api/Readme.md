# QuizePro

This is a simple Quiz application built using Flask and SQLite. The application provides multiple APIs for retrieving quiz questions, their possible answers, creating new questions, updating and deleting existing questions, and authenticating users.
## API endpoints

- `GET /quiz-info`: Get the size of the quiz and the list of scores.
- `GET /questions/all`: Get all the quiz questions along with their possible answers.
- `GET /questions/:id`: Get a specific quiz question by ID along with its possible answers.
- `POST /login`: Authenticate the user and return a JWT token.
- `GET /questions?position=<position>`: Get all questions with a specific position.
- `PUT /questions/<id>`: Update an existing question by ID.
-`POST /questions`: Create a new question.

## Requirements

- Requirements
- Python 3.x
- Flask
- Flask-CORS
- PyJWT
- SQLite3

## Dependencies

The application requires the following dependencies:

- Flask
- Flask-CORS
- PyJWT

## How to run the application

1. Install the dependencies by running `pip install -r requirements.txt`.
2. Run the application by executing `python app.py`.
3. Access the API endpoints through `http://localhost:5000`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.