from flask import Flask

app = Flask(__name__)

from worldhappinessapp import routes
