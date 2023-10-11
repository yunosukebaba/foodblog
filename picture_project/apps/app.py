"""
初期化処理
"""
from flask import Flask

# Flaskのインスタンスを生成
app = Flask(__name__)
# 設定ファイルを読み込む
app.config.from_pyfile('settings.py')

"""SQLAlchemyの登録
"""
# SQLAlchemyのインスタンスを生成
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# SQLAlchemyオブジェクトにflaskオブジェクトを登録する
db.init_app(app)

"""Migrateの登録
"""
# Migrateオブジェクトを生成して、
# FlaskオブジェクトとSQLAlchemyオブジェクトを登録する
from flask_migrate import Migrate
Migrate(app, db)

"""トップページのルーティング
"""
from flask import render_template
@app.route('/', methods=['GET', 'POST'])
def index():
    # index.htmlをレンダリングする
    return render_template('index.html')