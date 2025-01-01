from flask_security import auth_required, verify_password, hash_password
from flask import current_app as app, jsonify, request, render_template
from backend.models import db

datastore = app.security.datastore 

@app.route('/')
def home():
  return render_template('index.html')

@app.get('/protected')
@auth_required('token')
def protected():
    return'<h1> Only accessible by authenticated users</h1>'

@app.route('/login', methods = ['POST'])
def login():
  data = request.get_json()

  email = data.get('email')
  password = data.get('password')

  if not email or not password:
    return jsonify({'message' : "Invalid inputs"}), 404
  
  user = datastore.find_user(email = email)
  if not user:
    return jsonify({'message' : "Invalid email"}), 404
  
  if verify_password(password, user.password):
    return jsonify({'token': user.get_auth_token(), 'email': user.email, 'role': user.roles[0].name, 'id': user.id})
  
  return jsonify({'message' : "Invalid password"}), 404

from datetime import datetime

@app.route('/register', methods=['POST'])
def register():
  data = request.get_json()

  email = data.get('email')
  password = data.get('password')
  name = data.get('name')
  qualification = data.get('qualification')
  dob = data.get('dob')

  if not email or not password or not name or not qualification or not dob:
    return jsonify({'message': "Invalid inputs"}), 404

  user = datastore.find_user(email=email)
  if user:
    return jsonify({'message': "User already exists"}), 404

  try:
    dob = datetime.strptime(dob, "%Y-%m-%d").date()
    user_role = datastore.find_or_create_role(name='user', description='general user')
    datastore.create_user(
        email=email,
        password=hash_password(password),
        roles=[user_role],
        active=True,
        name=name,
        qualification=qualification,
        dob=dob
    )
    db.session.commit()
    return jsonify({'message': "User created"}), 200
  except Exception as e:
    db.session.rollback()
    return jsonify({'message': f"Error creating user: {str(e)}"}), 400

  

