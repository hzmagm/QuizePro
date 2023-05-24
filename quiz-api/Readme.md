# QuizePro

This is a simple Quiz application built using Flask and SQLite. The application provides multiple APIs for retrieving quiz questions, their possible answers, creating new questions, updating and deleting existing questions, and authenticating users, add participants and update the score.
## API endpoints

### Question Routes

- `GET /quiz-info`: Get the size of the quiz and the list of scores.
- `GET /questions/`: Get all the quiz questions along with their possible answers.
- `GET /questions/:id`: Get a specific quiz question by ID along with its possible answers.
- `GET /questions?position=<position>`: Get all questions with a specific position.

### Admin Routes ** LOGIN REQUIRED **

- `POST /admin/login`: Authenticate the user and return a token.
- `PUT /admin/questions/<id>`: Update an existing question by ID.
- `POST /admin/questions`: Create a new question.
- `DELETE /admin/questions/<id>` Delete all the possible answers associated with the question by Id 
- `DELETE /admin/questions/`: Delete all question.

### Participant Routes

- `GET /participations/all`: Get all the participants.
- `PUT /participations/<id>`: Update participant score by Id.
- `POST /participations/add`: Create a new participant.
- `GET /participations/:id`: Get a participant by Id.
- `GET /participations/all_ordered`: Get all participant ordered by score.

## Requirements

- autopep8==2.0.2
- click==8.1.3
- colorama==0.4.6
- Flask==2.2.3
- Flask-Cors==3.0.10
- greenlet==2.0.2
- gunicorn==20.1.0
- itsdangerous==2.1.2
- Jinja2==3.1.2
- MarkupSafe==2.1.2
- ORM-SQLite==0.0.2
- pycodestyle==2.10.0
- PyJWT==2.6.0
- six==1.16.0
- SQLAlchemy==2.0.10
- typing_extensions==4.5.0
- Werkzeug==2.2.3


## Dependencies

The application requires the following dependencies:

- Flask
- Flask-CORS
- PyJWT

## How to run the application

1. Install the dependencies by running `pip install -r requirements.txt`.
2. Run the application by executing `python app.py`.
3. Access the API endpoints through `http://localhost:5000`.

## Docker images

You can find the Docker images for this project on Docker Hub:

- [API Docker Image](https://hub.docker.com/r/hzmasbl/quiz-prod-api)
- [UI Docker Image](https://hub.docker.com/r/hzmasbl/quiz-prod-ui)

You can pull the image using the following command:

```bash
docker pull hzmasbl/quiz-prod-api
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
