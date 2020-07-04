import hashlib
from app import db


class JobOffer(db.Model):
    __tablename__ = "job_offers"

    id = db.Column(db.String(), primary_key=True)
    organization = db.Column(db.String())
    occupation = db.Column(db.String())
    job = db.Column(db.String())
    address = db.Column(db.String())
    search_date = db.Column(db.String())
    link = db.Column(db.String())
    lat = db.Column(db.String())
    lon = db.Column(db.String())

    def __init__(
        self, id, organization, occupation, job, address, search_date, link, lat, lon,
    ):
        self.id = id
        self.organization = organization
        self.occupation = occupation
        self.job = job
        self.address = address
        self.search_date = search_date
        self.link = link
        self.lat = lat
        self.lon = lon

    @classmethod
    def from_json(cls, json):
        return JobOffer(
            id=hashlib.md5(json["tyoavain"].encode("utf-8")).hexdigest(),
            organization=json["organisaatio"],
            occupation=json["ammattiala"],
            job=json["tyotehtava"],
            address=json["osoite"],
            search_date=json["haku_paattyy_pvm"],
            link=json["linkki"],
            lat=str(json["x"]),
            lon=str(json["y"]),
        )

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "organization": self.organization,
            "occupation": self.occupation,
            "job": self.job,
            "address": self.address,
            "search_date": self.search_date,
            "link": self.link,
            "lat": self.lat,
            "lon": self.lon,
        }
