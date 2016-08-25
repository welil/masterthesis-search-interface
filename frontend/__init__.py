import os

from flask import Flask
from flask.ext import assets
from flask.ext.compress import Compress

app = Flask(__name__)
app.config['COMPRESS_LEVEL'] = 1
Compress(app)

env = assets.Environment(app)

env.load_path = [
    os.path.join(os.path.dirname(__file__), 'sass')
]

env.register(
    'css_all',
    assets.Bundle(
        'all.sass',
        filters='sass',
        output='css_all.css'
    )
)
