from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db
from routes import recipes_bp
import time

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def retry_database_connection(max_retries=3, interval=5):
    retries = 0
    while retries < max_retries:
        try:
            with app.app_context():
                db.create_all()
            break
        except Exception as e:
            print(f"Failed to connect to database. Retrying in {interval} seconds...")
            time.sleep(interval)
            retries += 1
    else:
        print("Max retries reached. Unable to connect to database.")

retry_database_connection()

app.register_blueprint(recipes_bp, url_prefix='/recipes')

if __name__ in "__main__":
    app.run(debug=True)
