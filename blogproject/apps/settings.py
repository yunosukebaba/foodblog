import os

# モジュールの親ディレクトリのフルパスを取得
basedir = os.path.dirname(os.path.dirname(__file__))

# 親ディレクトリのblog.sqliteをデータベースに設定
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog.sqlite')

# シークレットキーの値として10バイトの文字列をランダムに生成
SECRET_KEY = os.urandom(10)


# 管理者のユーザー名とパスワード
USERNAME = 'admin'
PASSWORD = 'abcd1234'


# メール関連の設定---------------------------------------------------------------

# GmailのSMTPサーバー
MAIL_SERVER = 'smtp.gmail.com'
# メールサーバーのポート番号
MAIL_PORT = 587
# メールサーバーと通信する際にTLS(セキュア)接続を使う
MAIL_USE_TLS = True
# SSLを無効にする
MAIL_USE_SSL = False
# Gmailのメールアドレス
MAIL_USERNAME = 'yunosuke.baba1104@gmail.com'
# Gmailのアプリ用パスワード
MAIL_PASSWORD = 'dnsn dtie kisj yqlt'
# 送信元のメールアドレス
MAIL_DEFAULT_SENDER = 'yunosuke.baba1104@gmail.com'
# -----------------------------------------------------------------------------