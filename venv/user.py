from flask import Blueprint, jsonify
from controllers.userController import get_all_users

# Define Blueprint
user_bp = Blueprint('users', __name__)

# Route for getting all users
@user_bp.route('/', methods=['GET'])
def index():
    try:
        # Call the function to get all users
        users = get_all_users()
        
        # Return users in the response as JSON
        return jsonify({
            "success": True,
            "users": [user.to_dict() for user in users]  # Assuming users have a to_dict() method
        }), 200
    except Exception as e:
        # If there is an error, return an error message
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
