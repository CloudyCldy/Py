from models import User  
from database import db  
from config import db  # Import db from config.py



def get_all_users():
    return User.query.all()  


def user_by_id(user_id):
    return User.query.get(user_id)  


def delete_user(user_id):
    user = User.query.get(user_id)  
    if user:
        db.session.delete(user)  
        db.session.commit()  
        return f"Usuario con ID {user_id} ha sido eliminado"
    else:
        return f"Usuario con ID {user_id} no encontrado"


def create_user(user_data):
    """
    Create a new user in the database.
    
    Args:
        user_data (dict): A dictionary containing user data ('name' and 'email').

    Returns:
        User: The created user object or an error message.
    """
    try:
        # Create a new User instance
        new_user = User(**user_data)  # Unpack the user_data dictionary to User model

        # Add the new user to the session
        db.session.add(new_user)

        # Commit the transaction to save the user in the database
        db.session.commit()

        # Return the newly created user object
        return new_user
    except Exception as e:
        # Rollback the transaction if there is an error
        db.session.rollback()
        return f"Error al crear el usuario: {str(e)}"  # Return error message