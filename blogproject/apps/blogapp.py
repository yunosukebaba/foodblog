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
from sqlalchemy import select  # sqlalchemy.select()
from apps import models  # apps.modelsモジュール
from flask import render_template
from flask import request
from flask_paginate import Pagination, get_page_parameter

@app.route('/')
def index():
    # 投稿記事のレコードをidの降順で全件取得するクエリ
    stmt = select(
        models.Blogpost).order_by(models.Blogpost.id.desc())
    # データベースにクエリを発行
    entries = db.session.execute(stmt).scalars().all()

    # 現在のページ番号を取得
    page = request.args.get(
        get_page_parameter(), type=int, default=1)
    # entriesから現在のページに表示するレコードを抽出
    res = entries[(page - 1)*3: page*3]
    # Paginationオブジェクトを生成
    pagination = Pagination(
        page=page,
        total=len(entries),
        per_page=3)

    # index.htmlのレンダリングをする際にrowsオプションでレコードデータres、
    # paginationオプションでPaginationオブジェクトを引き渡す
    return render_template(
        'index.html',
        rows=res, pagination=pagination)

"""
詳細ページのルーティング
"""
@app.route('/entries/<int:id>')
def show_entry(id):
    # データベーステーブルから指定されたidのレコードを抽出
    entry = db.session.get(models.Blogpost, id)
    # 抽出したレコードをentry=entryに格納して
    # post.htmlをレンダリングする
    return render_template('post.html', entry=entry)


"""
問い合わせページのルーティングとビューの定義
フォームデータをメール送信する
"""
from flask import url_for, redirect   # url_for、redirect
from flask import flash   # flash
from apps import forms   # apps/forms.py

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # InquiryFormをインスタンス化
    form = forms.InquiryForm()
    if form.validate_on_submit():
        # フォームの入力データを取得
        username = form.username.data
        email = form.email.data
        message = form.message.data
        # メール送信
        send_mail(
            # 送信されたメールを受信するアドレス
            # Gmailで受信sる
            to='yunosuke.baba1104@gmail.com',
            # メールの表題
            subject="問い合わせページからのメッセージ",
            # templates/send_mail.txtをテンプレートに指定
            template="send_mail.txt",
            # ユーザー名、メールアドレス、メッセージ
            username=username,
            email=email,
            message=message
            )
        # フラッシュメッセージを表示
        flash('お問い合わせの内容は送信されました。')
        # 問い合わせ完了ページへ、リダイレクト
        return redirect(url_for("contact_complete"))
    
    # 問い合わせページをレンダリング
    return render_template('contact.html', form=form)

"""問い合わせ完了ページのルーティングとビューの定義
"""
@app.route('/contact_complete')
def contact_complete():
    # 問い合わせページをレンダリング
    return render_template('contact_complete.html')

"""flaskインスタンスをmailオブジェクトに登録
"""
from flask_mail import Mail
mail = Mail(app)

from flask_mail import Message
def send_mail(to, subject, template, **kwargs):
    """メールを送信する
    
    Args:
        to: Mailの送信先
        subject: メールの表題
        template: メール本文に適用するテンプレート
        **kwargs: 複数のキーワード引数を辞書として受け取る
    """
    # Messageオブジェクトを生成
    # 表題を第1引数、送信先をrecipientsオプションで指定
    msg = Message(subject, recipients=[to])
    # メール本文のテンプレートをレンダリングして
    # メッセージボディmsg.bodyに格納
    msg.body = render_template(template, **kwargs)
    # メールの送信
    # msgを引数にしてMailオブジェクトからsend()メソッドを実行
    mail.send(msg)


"""
ブループリントの登録
"""
# crudアプリのモジュールviews.pyからBlueprint[crud]をインポート
from apps.crud.views import crud

# FlaskオブジェクトにBlueprint[crud]を登録
app.register_blueprint(crud)