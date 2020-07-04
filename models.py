from app import db


class JobOffer(db.Model):
    __tablename__ = 'job_offers'

    id = db.Column(db.Integer(), primary_key=True)
    organization = db.Column(db.String())
    occupation = db.Column(db.String())
    job = db.Column(db.String())
    address = db.Column(db.String())
    search_date_date = db.Column(db.String())
    link = db.Column(db.String())
    lat = db.Column(db.Numeric())
    lon = db.Column(db.Numeric())

    def __init__(self, organization, occupation, job, address, search_date_date, link, lat, lon):
        self.organization = organization
        self.occupation = occupation
        self.job = job
        self.address = address
        self.search_date_date = search_date_date
        self.link = link
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'organization': self.organization,
            'occupation': self.occupation,
            'job': self.job,
            'address': self.address,
            'search_date_date': self.search_date_date,
            'link': self.link,
            'lat': self.lat,
            'lon': self.lon,
        }

