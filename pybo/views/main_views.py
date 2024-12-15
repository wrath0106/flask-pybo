from flask import  Blueprint, redirect, url_for

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'hello, pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question.list'))