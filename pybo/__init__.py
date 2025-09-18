from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# database 등록
db = SQLAlchemy()
migrate = Migrate()

def create_app():  # 애플리케이션 팩토리
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루 프린트를 등록
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app