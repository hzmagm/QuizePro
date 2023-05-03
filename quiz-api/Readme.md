# QuizePro

This is a simple Quiz application built using Flask and SQLite. The application provides multiple currently it provides API to retrieve quiz questions, their possible answers and also to authenticate users.

## API endpoints

- `GET /quiz-info`: Get the size of the quiz and the list of scores.
- `GET /questions`: Get all the quiz questions along with their possible answers.
- `GET /questions/:id`: Get a specific quiz question by ID along with its possible answers.
- `POST /login`: Authenticate the user and return a JWT token.

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