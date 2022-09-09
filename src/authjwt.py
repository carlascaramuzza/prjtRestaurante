

from routes import conexao




def user_by_username(username):
    try:
        cursor = conexao.connection.cursor()
        sql = "SELECT username, senha  FROM usuario WHERE username = '{0}';".format(username)
        cursor.execute(sql)
        dados = cursor.fetchone()
        return dados
    except:
        return None       

    


#def token_required(f):
 #   @wraps(f)
  #  def decorated(*args, **kwargs):
   #     token = request.args.get('token')
    #    if not token:
     #       return jsonify({'message': 'token is missing', 'data': []}), 401
      #  try:
       #     data = token.decode(token, app.config['SECRET_KEY'])
        #    current_user = user_by_username(username=data['username'])
        #except:
         #   return jsonify({'message': 'token is invalid or expired', 'data': []}), 401
        #return f(current_user, *args, **kwargs)
    #return decorated


# Gerando token com base na Secret key do app e definindo expiração com 'exp'
