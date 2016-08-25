from flask.ext.elasticsearch import FlaskElasticsearch

from frontend import app

es_instance = FlaskElasticsearch()
es_instance.init_app(app)
