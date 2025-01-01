from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)
	name = db.Column(db.String, nullable=False)
	qualification = db.Column(db.String, nullable=False)
	dob = db.Column(db.Date, nullable=False)

	# Flask-Security specific fields
	fs_uniquifier = db.Column(db.String, unique=True, nullable=False)
	active = db.Column(db.Boolean, default=True)
	roles = db.relationship('Role', backref='bearers', secondary='user_roles')

class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True, nullable=False)
	description = db.Column(db.String, nullable=False)

class UserRoles(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
	role_id = db.Column(db.Integer, db.ForeignKey('role.id', ondelete='CASCADE'), nullable=False)

class Subject(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False, unique=True)
	description = db.Column(db.Text, nullable=True)

class Chapter(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	subject_id = db.Column(db.Integer, db.ForeignKey('subject.id', ondelete='CASCADE'), nullable=False)
	name = db.Column(db.String(255), nullable=False)
	description = db.Column(db.Text, nullable=True)
	subject = db.relationship('Subject', backref=db.backref('chapters', lazy=True, cascade="all, delete-orphan"))

class Quiz(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id', ondelete='CASCADE'), nullable=False)
	date_of_quiz = db.Column(db.Date, nullable=False)
	time_duration = db.Column(db.Time, nullable=False)
	remarks = db.Column(db.Text, nullable=True)
	chapter = db.relationship('Chapter', backref=db.backref('quizzes', lazy=True, cascade="all, delete-orphan"))

class Question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id', ondelete='CASCADE'), nullable=False)
	question_statement = db.Column(db.Text, nullable=False)
	option1 = db.Column(db.String(255), nullable=False)
	option2 = db.Column(db.String(255), nullable=False)
	option3 = db.Column(db.String(255), nullable=True)
	option4 = db.Column(db.String(255), nullable=True)
	correct_option = db.Column(db.Integer, nullable=False)
	quiz = db.relationship('Quiz', backref=db.backref('questions', lazy=True, cascade="all, delete-orphan"))

class Score(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id', ondelete='CASCADE'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
	time_stamp = db.Column(db.DateTime, nullable=False, index=True, default=datetime.now)
	total_scored = db.Column(db.Float, nullable=False)
	quiz = db.relationship('Quiz', backref=db.backref('scores', lazy=True, cascade="all, delete-orphan"))
	user = db.relationship('User', backref=db.backref('scores', lazy=True, cascade="all, delete-orphan"))
