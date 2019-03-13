from app import db
from sqlalchemy import Column, Integer, String

class Blog(db.Model):


    __tablename__ = "posts"


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)


    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return '{}--{}'.format(self.id, self.title)