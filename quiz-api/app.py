from flask import Flask
from flask_cors import CORS
from dummy_data import *
from routes import questions_routes
from models import db

app = Flask(__name__)
app.secret_key="test secret"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///quizeTest.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["JSON_SORT_KEYS"] = False
CORS(app)

db.init_app(app)

app.register_blueprint(questions_routes)

@app.before_first_request
def create_tables():
    db.drop_all()
    db.create_all()
    creat_dummy_data()

if __name__ == "__main__":
    create_tables()
    app.run()