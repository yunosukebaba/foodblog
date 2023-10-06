from flask import Flask

# Flaskのインスタンスを生成
app = Flask(__name__)

# 設定ファイルを読み込む
app.config.from_pyfile('settings.py')

# SQLAlchemyのインスタンスを生成
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# SQLAlchemyオブジェクトにFlaskオブジェクトを登録する
db.init_app(app)

# Migrateオブジェクトを生成して
# FlaskオブジェクトとSQLAlchemyオブジェクトを登録する
from flask_migrate import Migrate
Migrate(app,db)

# トップページのルーティング
from flask import render_template

@app.route('/')
def index():
    # index.htmlをレンダリングして返す
    return render_template('index.html')

"""
ブループリントの登録
"""
# crudアプリのモジュールviews.pyからBlueprint[crud]をインポート
from apps.crud.views import crud

# FlaskオブジェクトにBlueprint[crud]を登録
app.register_blueprint(crud)