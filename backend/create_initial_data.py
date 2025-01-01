from flask import current_app as app
from backend.models import db, User, Role
from flask_security import SQLAlchemyUserDatastore, hash_password
from datetime import date

with app.app_context():
    db.create_all()

    user_data: SQLAlchemyUserDatastore = app.security.datastore

    admin_role = user_data.find_or_create_role(name='admin', description='superuser')
    user_role = user_data.find_or_create_role(name='user', description='general user')  

    if not user_data.find_user(email="admin@gmail.com"):
        user_data.create_user(
            email="admin@gmail.com", password= hash_password("pass"), name="Admin", 
            qualification="Admin", dob=date(1998, 12, 30), roles=[admin_role] 
        )

    if not user_data.find_user(email="user01@gmail.com"):
        user_data.create_user(
            email="user01@gmail.com", password=hash_password("pass1"), name="User 01", 
            qualification="1st year", dob=date(2010, 11, 30), roles=[user_role] 
        )

    if not user_data.find_user(email="user02@gmail.com"):
        user_data.create_user(
            email="user02@gmail.com", password= hash_password("pass2"), name="User 02", 
            qualification="2nd year", dob=date(2009, 12, 29), roles=[user_role]  
        )

    db.session.commit()  