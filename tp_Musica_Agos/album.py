from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort


from tp_Musica_Agos.db import get_db

bp = Blueprint('album', __name__)

@bp.route('/album')
def index():
    db = get_db()
    album = db.execute(
        """SELECT a.Title AS Album
         FROM genres g JOIN tracks t ON t.GenreId = g.GenreId
		 JOIN albums a ON a.AlbumId =  t.AlbumId
		 JOIN artists ar ON a.ArtistId = ar.ArtistId
         GROUP BY a.AlbumId"""
    ).fetchall()
    return render_template('album/alb.html', album=album)

def get_album(id):
    album = get_db().execute(
        """SELECT a.Title AS Album
         FROM genres g JOIN tracks t ON t.GenreId = g.GenreId
		 JOIN albums a ON a.AlbumId =  t.AlbumId
		 JOIN artists ar ON a.ArtistId = ar.ArtistId
         GROUP BY a.AlbumId""",
        (id,)
    ).fetchone()
    if album is None:
        abort(404, f"album id {id} doesn't exist.")

    return album