import string
import random


random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))

class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Projetoccljr2022*'
    MYSQL_DB = 'restaurante'
    SECRET_KEY = key

config ={
    'development': DevelopmentConfig
}