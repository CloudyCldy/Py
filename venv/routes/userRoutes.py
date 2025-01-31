from flask import Blueprint, jsonify, request
from controllers.userController import get_all_users, user_by_id, create_user, delete_user
from models import User
from config import db


user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    """
    Ruta para obtener todos los usuarios.
    """
    try:
        users = get_all_users()  
        return jsonify({"success": True, "users": [user.to_dict() for user in users]}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """
    Ruta para obtener un usuario por su ID.
    """
    try:
        user = user_by_id(user_id)  
        if isinstance(user, str):  
            return jsonify({"success": False, "message": user}), 404
        return jsonify({"success": True, "user": user.to_dict()}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@user_bp.route('/', methods=['POST'])
def create_new_user():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Extract 'name' and 'email' from the data
        name = data.get("name")
        email = data.get("email")

        # Validate that both 'name' and 'email' are provided
        if not name or not email:
            return jsonify({
                "success": False,
                "message": "Faltan campos requeridos (name, email)."
            }), 400

        # Create a dictionary with the user data
        user_data = {"name": name, "email": email}

        # Call the create_user function to create the user
        user = create_user(user_data)

        # Check if the user was created successfully
        if isinstance(user, User):  # If the returned value is a User object
            return jsonify({
                "success": True,
                "user": user.to_dict()  # Return the user data as a dictionary
            }), 201
        else:
            # If there's an error, return the error message from create_user()
            return jsonify({
                "success": False,
                "message": user
            }), 500
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    """
    Ruta para eliminar un usuario por su ID.
    """
    try:
        result = delete_user(user_id)  
        if "eliminado" in result:  
            return jsonify({"success": True, "message": result}), 200
        else:  
            return jsonify({"success": False, "message": result}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user_by_id(user_id):
    """
    Ruta para actualizar un usuario por su ID.
    """
    try:
        data = request.get_json()  
        name = data.get("name")
        email = data.get("email")
        if not name or not email:
            return jsonify({"success": False, "message": "Faltan campos requeridos (name, email)."}), 400
        
        user = user_by_id(user_id)  
        if isinstance(user, str):  
            return jsonify({"success": False, "message": user}), 404
        
        
        user.name = name
        user.email = email
        db.session.commit()  
        return jsonify({"success": True, "user": user.to_dict()}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
