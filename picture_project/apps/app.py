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
from flask import render_template, url_for, redirect, flash
from apps import models
from apps import forms

@app.route('/', methods=['GET', 'POST'])
def index():
    # SignupFormをインスタンス化
    form = forms.SignupForm()
    # サインアップフォームのsubmitボタンが押されたときの処理
    if form.validate_on_submit():
        # モデルクラスUserのインスタンスを生成
        user = models.User(
            # フォームのusernameに入力されたデータを取得してUserのusernameフィールドに格納
            username=form.username.data,
            # フォームのemailに入力されたデータを取得してUserのemailフィールドに格納
            email=form.email.data,
            # フォームのpasswordに入力されたデータを取得してUserのpasswordプロパティに格納
            password=form.password.data,
        )
        # メールアドレスの重複チェック
        if user.is_duplicate_email():
            # メールアドレスがすでに登録済みの場合は
            # メッセージを表示してエンドポイントindexにリダイレクト
            flash("登録済みのメールアドレスです")
            return redirect(url_for('index'))
        
        # Userオブジェクトをレコードのデータとして
        # データベースのテーブルに追加
        db.session.add(user)
        # データベースを更新
        db.session.commit()
        # 処理完了後、エンドポイントindexにリダイレクト
        return redirect(url_for('index'))
    
    # トップページへのアクセスは、index.htmlをレンダリングして
    # SignupFormのインスタンスformを引き渡す
    return render_template('index.html', form=form)