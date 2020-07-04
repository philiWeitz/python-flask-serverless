import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_HOST = os.environ['POSTGRES_HOST']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://%s:%s@%s:%s/%s' % (
        POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB)

db = SQLAlchemy(app)

from models import JobOffer

@app.route("/health")
def health():
    jobOffer = JobOffer(
        organization='a',
        occupation='a',
        job='a',
        address='a',
        search_date_date='a',
        link='a',
        lat=1,
        lon=2
    )

    try:
        db.session.add(jobOffer)
        db.session.commit()
    except Exception as e:
        return (str(e))

    return jsonify({'status': 'OK'})


if __name__ == '__main__':
    app.run()
