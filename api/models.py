# db instance form init file
from api import db, ma

class Movie(db.Model):
    __tablename__ = "netflix_titles"
    show_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text)
    title = db.Column(db.Text)
    director = db.Column(db.Text)
    cast = db.Column(db.Text)
    country = db.Column(db.Text)
    date_added = db.Column(db.DateTime)
    release_year = db.Column(db.Integer)
    rating = db.Column(db.Text)
    duration = db.Column(db.Text)
    listed_in = db.Column(db.Text)
    description = db.Column(db.Text)
    # how to call raw sql
    # rs = db.engine.execute('SELECT * FROM netflix_titles')



# Setup Movie Class Schema
class MovieSchema(ma.Schema):
  class Meta:
    fields = ('show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description')