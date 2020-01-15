from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.Integer(120), unique=False, nullable=False)
    petname = db.relationship('DogUser', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.firstName

    def serialize(self):
        return {
            "firstName": self.firstName,
            "email": self.email,
            "password": self.password,
            "date": self.date
    }
class DogUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer(120), unique=False, nullable=False)
    breed_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    img = db.Column(db.String(120), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
     
    def __repr__(self):
        return '<DogUser %r>' % self.Name

    def serialize(self):
        return {
            "Name": self.Name,
            "age": self.age,
            "breed": self.breed,
            "img": self.img
    }