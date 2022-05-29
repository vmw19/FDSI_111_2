from flask import Flask


app = Flask(__name__)


@app.get("/")
def index():
    me = {
        "first_name": "Vicki",
        "last_name": "Warren",
        "hobbies": "power walking"
    }
    return me