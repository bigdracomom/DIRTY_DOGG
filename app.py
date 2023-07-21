from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy()
db.init_app(app)

class item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    avatar_url = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route('/signup')
def signup():
    return render_template('sign-up.html')
@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    if request.method == 'POST':
        user_name = request.form['Name']
        user_password = request.form['Password']
        user_email = request.form['Email']
        new_user = User(name=user_name, password=user_password, email=user_email)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect("/users")
        except:
            return 'There was an issue signing up'
    else:
        return render_template('checkout.html')
@app.route('/users', methods=['GET'])
def users():
    users = User.query.order_by(User.date_created).all()
    print(len(users))
    return render_template('users.html', users=users)
    
if (__name__ == "__main__"):
    app.run(debug=True)



















