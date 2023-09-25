@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT GenreId, name FROM genres'
    ).fetchall()
    return render_template('music/index.html', posts=posts)