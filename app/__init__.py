from flask import Flask
app = Flask(__name__)
app.secret_key = '!MY-FIRST-CODE-DEMO!'

from app import routes
