from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from tp_Musica_Agos.db import get_db

bp = Blueprint('tracks', __name__, url_prefix="/track")

@bp.route('/')
def index():
    db = get_db()
    tracks = db.execute(
        """SELECT t.name AS Titulo  , t.trackId
         FROM genres g JOIN tracks t ON t.GenreId = g.GenreId
		 JOIN albums a ON a.AlbumId =  t.AlbumId
		 JOIN artists ar ON a.ArtistId = ar.ArtistId"""
    ).fetchall()
    return render_template('tracks/index.html', tracks=tracks)

def get_track(id):
    tracks = get_db().execute(
        """SELECT t.name AS Titulo
         FROM genres g JOIN tracks t ON t.GenreId = g.GenreId
		 JOIN albums a ON a.AlbumId =  t.AlbumId
		 JOIN artists ar ON a.ArtistId = ar.ArtistId""",
        (id,)
    ).fetchone()
    if tracks is None:
        abort(404, f"tracks id {id} doesn't exist.")

    return tracks

@bp.route('/<int:id>')
def detalle(id):
    db = get_db()
    track = db.execute(
        """SELECT t.name AS Titulo 
         FROM tracks t 
         WHERE t.trackId = ?""",
         (id,)
    ).fetchone()
    return render_template('tracks/detalle.html', track=track)