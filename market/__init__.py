from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '2e5dd869959291693f411990'


app.app_context().push()

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from market import routes






