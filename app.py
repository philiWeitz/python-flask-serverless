import os
import requests
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
POSTGRES_PORT = os.environ["POSTGRES_PORT"]
POSTGRES_DB = os.environ["POSTGRES_DB"]
POSTGRES_HOST = os.environ["POSTGRES_HOST"]

app.config["DEBUG"] = True
app.config["DEVELOPMENT"] = True

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://%s:%s@%s:%s/%s" % (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB,
)

db = SQLAlchemy(app)

from models import JobOffer


@app.route("/health")
def health():
    return {"status": "OK"}


@app.route("/jobs")
def get_jobs():
    try:
        jobs = JobOffer.query.all()
        return jsonify([e.serialize() for e in jobs])
    except Exception as e:
        abort(500, e)


@app.route("/jobs/<id>")
def get_job_by_id(id):
    try:
        job_offer = JobOffer.query.filter_by(id=id).first()
        if not job_offer:
            abort(404, description="No job found with this id")

        return jsonify(job_offer.serialize())
    except Exception as e:
        abort(500, e)


@app.route("/fetch-jobs")
def fetch_jobs():
    response = requests.get("http://gis.vantaa.fi/rest/tyopaikat/v1/kaikki")
    job_offers = [JobOffer.from_json(job_json) for job_json in response.json()]

    try:
        db.session.add_all(job_offers)
        db.session.commit()
        return ""
    except Exception as e:
        abort(500, e)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e.description), code=404), 404


@app.errorhandler(500)
def resource_not_found(e):
    return jsonify(error=str(e.description), code=500), 500


if __name__ == "__main__":
    app.run()
