from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class InquiryForm(FlaskForm):
    """問い合わせページのフォームクラス
    
    Attributes:
        username: ユーザー名
        email: メールアドレス
        message: 問い合わせ内容
        submit: 送信ボタン
    """
    username = StringField(
        "ユーザー名",
        validators=[DataRequired(message="入力が必要です。")])
    
    email = StringField(
        "メールアドレス",
        validators=[DataRequired(message="入力が必要です。"),
                    Email(message="メールアドレスの形式で入力してください。"),])
    
    message = TextAreaField(
        "メッセージ",
        validators=[DataRequired(message="入力が必要です。"),])
    
    # フォームのsubmitボタン
    submit = SubmitField(("送信"))