from flask import Flask
from config import db,migrate #migaciones
from routes.user import 
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite://app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app)
migrate-init_app(app,db)

app.register_blueprint(user_bp,url_prefix='users')
if __name__ = '__main__':
app.run(debug=True)