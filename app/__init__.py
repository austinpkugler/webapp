import dotenv
from flask import Flask

import os


dotenv.load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')


from app import routes
