# Import the __init__.py from modules which had imported all files from the folder.
import modules
from flask import Flask

# Define app.
app = Flask(__name__)
