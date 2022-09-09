from flask import jsonify, request
from authjwt import user_by_username
from werkzeug.security import check_senha_hash
import datetime
import config


def authentication():
    auth = request.authorization
    if not auth or not auth.username or not auth.senha:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'user not found', 'data': []}), 401

    if user and check_senha_hash(user.senha, auth.senha):
        token = token.encode({'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) },
                           config['SECRET_KEY'])
        return jsonify({'message': 'Validated successfully', 'token': token.decode('UTF-8'),
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
