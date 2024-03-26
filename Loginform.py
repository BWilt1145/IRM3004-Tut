from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'Sejcret@ufvnr'

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)

@app.route('/')
def home():
    return render_template('Loginform.html')

@app.route('/database')
def database():
    return render_template('database.db')

if __name__ == "__main__":
    app.run(debug=True)