from flask_restful import Api, Resource, fields, marshal_with
from flask_security import auth_required
from flask import request
from backend.models import db, Subject, Chapter, Quiz, Question

api = Api(prefix='/api')

subject_fields = {
  'id': fields.Integer,
  'name': fields.String,
  'description': fields.String,
}

chapter_fields = {
  'id': fields.Integer,
  'name': fields.String,
  'description': fields.String,
  'subject_id': fields.Integer,
}

quiz_fields = {
  'id': fields.Integer,
  'chapter_id': fields.Integer,
  'date_of_quiz': fields.DateTime,
  'time_duration': fields.DateTime,
  'remarks': fields.String,
}

question_fields = {
  'id': fields.Integer,
  'quiz_id': fields.Integer,
  'question_statement': fields.String,
  'option1': fields.String,
  'option2': fields.String,
  'option3': fields.String,
  'option4': fields.String,
  'correct_option': fields.Integer,
}

# Resources
class SubjectAPI(Resource):
  @marshal_with(subject_fields)
  @auth_required('token')
  def get(self):
    subjects = Subject.query.all()
    if not subjects:
      return {"message": "No subjects found"}, 404
    return subjects, 200

  @auth_required('token')
  def post(self):
    data = request.get_json()
    print(data)
    subject = Subject(name=data.get('name'), description=data.get('description'))
    db.session.add(subject)
    db.session.commit()
    return {"message": "Subject created successfully", "id": subject.id}, 201

  @auth_required('token')
  def delete(self, subject_id):
    subject = Subject.query.get_or_404(subject_id)
    db.session.delete(subject)
    db.session.commit()
    return {"message": "Subject deleted successfully"}, 200

  @auth_required('token')
  def put(self, subject_id):
    data = request.get_json()
    subject = Subject.query.get_or_404(subject_id)
    subject.name = data.get('name')
    subject.description = data.get('description')
    db.session.commit()
    return {"message": "Subject updated successfully"}, 200

class ChapterAPI(Resource):
  @marshal_with(chapter_fields)
  @auth_required('token')
  def get(self, subject_id):
    chapters = Chapter.query.filter_by(subject_id=subject_id).all()
    if not chapters:
      return {"message": "No chapters found for this subject"}, 404
    return chapters, 200

  @auth_required('token')
  def post(self, subject_id):
    data = request.get_json()
    chapter = Chapter(
      subject_id=subject_id,
      name=data.get('name'),
      description=data.get('description')
    )
    db.session.add(chapter)
    db.session.commit()
    return {"message": "Chapter created successfully", "id": chapter.id}, 201

  @auth_required('token')
  def delete(self, chapter_id):
    chapter = Chapter.query.get_or_404(chapter_id)
    db.session.delete(chapter)
    db.session.commit()
    return {"message": "Chapter deleted successfully"}, 200

  @auth_required('token')
  def put(self, chapter_id):
    data = request.get_json()
    chapter = Chapter.query.get_or_404(chapter_id)
    chapter.name = data.get('name')
    chapter.description = data.get('description')
    db.session.commit()
    return {"message": "Chapter updated successfully"}, 200

class QuizAPI(Resource):
  @marshal_with(quiz_fields)
  @auth_required('token')
  def get(self, chapter_id):
    quizzes = Quiz.query.filter_by(chapter_id=chapter_id).all()
    if not quizzes:
      return {"message": "No quizzes found for this chapter"}, 404
    return quizzes, 200

  @auth_required('token')
  def post(self, chapter_id):
    data = request.get_json()
    quiz = Quiz(
      chapter_id=chapter_id,
      date_of_quiz=data.get('date_of_quiz'),
      time_duration=data.get('time_duration'),
      remarks=data.get('remarks')
    )
    db.session.add(quiz)
    db.session.commit()
    return {"message": "Quiz created successfully", "id": quiz.id}, 201

  @auth_required('token')
  def delete(self, quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    db.session.delete(quiz)
    db.session.commit()
    return {"message": "Quiz deleted successfully"}, 200

  @auth_required('token')
  def put(self, quiz_id):
    data = request.get_json()
    quiz = Quiz.query.get_or_404(quiz_id)
    quiz.date_of_quiz = data.get('date_of_quiz')
    quiz.time_duration = data.get('time_duration')
    quiz.remarks = data.get('remarks')
    db.session.commit()
    return {"message": "Quiz updated successfully"}, 200

class QuestionAPI(Resource):
  @marshal_with(question_fields)
  @auth_required('token')
  def get(self, quiz_id):
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    if not questions:
      return {"message": "No questions found for this quiz"}, 404
    return questions, 200

  @marshal_with(question_fields)
  @auth_required('token')
  def get_single(self, question_id):
    question = Question.query.get_or_404(question_id)
    return question, 200

  @auth_required('token')
  def post(self, quiz_id):
    data = request.get_json()
    question = Question(
      quiz_id=quiz_id,
      question_statement=data.get('question_statement'),
      option1=data.get('option1'),
      option2=data.get('option2'),
      option3=data.get('option3'),
      option4=data.get('option4'),
      correct_option=data.get('correct_option')
    )
    db.session.add(question)
    db.session.commit()
    return {"message": "Question created successfully", "id": question.id}, 201

  @auth_required('token')
  def delete(self, question_id):
    question = Question.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    return {"message": "Question deleted successfully"}, 200

  @auth_required('token')
  def put(self, question_id):
    data = request.get_json()
    question = Question.query.get_or_404(question_id)
    question.question_statement = data.get('question_statement')
    question.option1 = data.get('option1')
    question.option2 = data.get('option2')
    question.option3 = data.get('option3')
    question.option4 = data.get('option4')
    question.correct_option = data.get('correct_option')
    db.session.commit()
    return {"message": "Question updated successfully"}, 200

# Add resources
api.add_resource(SubjectAPI, '/subjects', '/subjects/<int:subject_id>')
api.add_resource(ChapterAPI, '/subjects/<int:subject_id>/chapters', '/chapters/<int:chapter_id>')
api.add_resource(QuizAPI, '/chapters/<int:chapter_id>/quizzes', '/quizzes/<int:quiz_id>')
api.add_resource(QuestionAPI, '/quizzes/<int:quiz_id>/questions', '/questions/<int:question_id>')