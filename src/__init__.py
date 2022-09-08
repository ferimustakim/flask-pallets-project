import os
from flask import Flask
from . import db
from . import auth
from . import blog

def create_app(test_config=None):
    #membuat app dan confignya disini
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = os.path.join(app.instance_path, 'inventaris.sqlite'),
    )

    if test_config is None:
        #menjalankan instance config, jika ada
        app.config.from_pyfile('config.py', silent=True)
    else:
        #menjalankan test config 
        app.config.from_mapping(test_config)

    #memastikan folder instance ada
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #menampilkan halaman page 
    #@app.route('/hello')
    #def hello():
     #   return 'Hello, guysss'
    
    #db.app=app
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app