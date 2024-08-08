from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(10))
    address = db.Column(db.String(100))
    education = db.Column(db.String(100))
    experience = db.Column(db.String(100))

    def __init__(self, name, email, phone,address,education,experience):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.education = education
        self.experience = experience

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password