"""
Archivo principal de la aplicación Flask
"""
import os
from flask import Flask
from flask_restful import Api
from models import db
from config import config
from resources.video import VideoListResource

def create_app(config_name='default'):
    """
    Función factory para crear la aplicación Flask
    
    Args:
        config_name (str): Nombre de la configuración a utilizar
        
    Returns:
        Flask: Aplicación Flask configurada
    """
    # TODO: Crear el objeto 'app'
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(config[config_name])
    
    # Inicializar extensiones
    db.init_app(app)
    api = Api(app)
    
    # Registrar rutas
    api.add_resource(VideoListResource, "/api/videos", "/api/videos/<int:video_id>")
    return app

if __name__ == "__main__":
    # Obtener configuración del entorno o usar 'development' por defecto
    config_name = os.getenv('FLASK_CONFIG', 'development')
    
    # Crear aplicación
    app = create_app(config_name)
    
    # Crear todas las tablas en la base de datos
    with app.app_context():
        db.create_all()
    
    # Ejecutar servidor
    app.run(host='0.0.0.0', port=5000)

