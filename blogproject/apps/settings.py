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