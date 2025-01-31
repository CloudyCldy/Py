from config import db
from models.User import User

# Crear las tablas en la base de datos
if __name__ == '__main__':
    db.create_all()
    print("Tablas creadas exitosamente.")
