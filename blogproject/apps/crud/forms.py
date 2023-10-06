from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class AdminForm(FlaskForm):
    """
    ログイン画面のフォームクラス
    
    Attributes:
        username: ユーザー名
        password: パスワード
        submit: 送信ボタン
    """
    username = StringField(
        "管理者名",
        validators=[DataRequired(message="入力が必要です。")]
    )
    password = PasswordField(
        "パスワード",
        validators=[DataRequired(message="入力が必要です。")]
    )
    # フォームのsubmitボタン
    submit = SubmitField(("ログイン"))


class ArticlePost(FlaskForm):
    """
    投稿ページのフォームクラス
    
    Attributes:
        post_title: タイトル
        post_contents: 本文
        submit: 送信ボタン
    """
    post_title = StringField(
        "タイトル",
        validators=[DataRequired(message="入力が必要です。"),]
    )
    post_contents = TextAreaField(
        "本文",
        validators=[DataRequired(message="入力が必要です。"),]
    )
    # フォームのsubmitボタン
    submit = SubmitField(("投稿する"))