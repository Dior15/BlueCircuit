from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session

class UserLogin:
    def signup(email, username, password, confirmPassword):
        if not email or not username or not password or not confirmPassword:
            return {'success': False, 'message': 'Username and password are required'}, 400
        
        if password != confirmPassword:
            return {'success' : False, 'message': 'Passwords do not match'}, 400
        
        # Check if user exists
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return {'success': False, 'message': 'User already exists'}, 409
        
        
        #Hash the passwords and save the user
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
    
        return {'success': True, 'message': 'Signup successful!'}, 201
    
    
    def login(username, password):
        if not username or not password:
            return {'success': False, 'message':'Username and password are required'}, 400
        
        user = User.query.filter((User.username == username) | (User.email == username)).first()
        if not user: 
            return {'success': False, 'message':'User does not exist'}, 404
        
        # Check the hashed password
        if not check_password_hash(user.password_hash, password):
            return {'success': False, 'message' : 'Incorrect password'}, 401
        
        session['user_id'] = user.id
        return {'success': True, 'message': 'Login successful!'}, 200
    
    def logout():
        session.pop('user_id', None)
        return {'success': True, 'message': 'Logged out successfully'}, 200
    
    def check_login():
        if 'user_id' in session:
            user = User.query.get(session['user_id'])
            return {'logged_in': True, 'user': user.username}, 200
        return {'logged_in': False}, 200