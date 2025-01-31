from flask import Flask
from config import db, init_db  # Import db and init_db function
from routes.userRoutes import user_bp  # Import your user routes blueprint

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/python'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
init_db(app)

# Register the routes
app.register_blueprint(user_bp, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)
