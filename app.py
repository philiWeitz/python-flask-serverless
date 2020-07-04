import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from config import ProductionConfig
from dotenv import load_dotenv

app = Flask(__name__)

# load env variables from .aws.env file
load_dotenv()

# use production config by default
app.config.from_object(os.environ['APP_SETTINGS'] or ProductionConfig)
db = SQLAlchemy(app)


@app.route("/health")
def health():
    return "Healthy"


@app.route("/book")
def book():
    return "Hello World!"


if __name__ == '__main__':
    app.run()