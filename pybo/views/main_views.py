from flask import Blueprint

# 블루 프린트 : 라우팅 함수를 관리하는 역할
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hello_pybo():
    return 'Hello Pybo!'

@bp.route('/hello')
def hello_world():
    return 'Hello World~!'