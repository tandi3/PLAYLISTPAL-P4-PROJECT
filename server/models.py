from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from config import db

class Playlist(db.Model, SerializerMixin):
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    serialize_rules = ('-id',)

    def __repr__(self):
        return f'<Playlist {self.name}>'
