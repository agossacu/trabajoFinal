from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from tp_Musica_Agos.db import get_db

bp = Blueprint('artist', __name__, url_prefix='/artist')

@bp.route('/artist')
def index():
    db = get_db()
    artista = db.execute(
        """SELECT ar.Name AS Artista
         FROM genres g JOIN tracks t ON t.GenreId = g.GenreId
		 JOIN albums a ON a.AlbumId =  t.AlbumId
		 JOIN artists ar ON a.ArtistId = ar.ArtistId
         GROUP BY ar.ArtistId"""
    ).fetchall()
    return render_template('artist/art.html', artista=artista)

def get_artist(id):
    artist = get_db().execute(
        """SELECT ar.Name AS Artista
         FROM genres g JOIN tracks t ON t.GenreId = g.GenreId
		 JOIN albums a ON a.AlbumId =  t.AlbumId
		 JOIN artists ar ON a.ArtistId = ar.ArtistId
         GROUP BY ar.ArtistId""",
        (id,)
    ).fetchone()
    if artist is None:
        abort(404, f"artist id {id} doesn't exist.")

    return artist