from flask import Blueprint ,render_template

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def hello():
    return 'Hello, Flask!'

@bp.route('/main')
def main():
    import parsing.naver_movie as nm
    return render_template('/main.html', movie_list=nm.naver_movies, text='main_text')

