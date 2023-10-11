from datetime import datetime
# werkzeug.securityからパスワード関連の関数をインポート
from werkzeug.security import generate_password_hash, check_password_hash
# flask_loginからUserMixinクラスをインポート
from flask_login import UserMixin
# app.pyからSQLAlchemyのインスタンスdbをインポート
from apps.app import db


class User(db.Model, UserMixin):
    """モデルクラス
        db.ModelとUserMixinを継承"""
    # テーブル名を「users」にする
    __tablename__="users"

    # 自動的に連番を振るフィールド、プライマリーキー
    id = db.Column(
        db.Integer,             # Integer型
        primary_key=True,       # プライマリーキーに設定
        autoincrement=True)     # 自動連番を振る
    
    # ユーザー名用のフィールド
    username = db.Column(
        db.String(30),          # String型(最大文字数30)
        index=True,             # インデックス
        nullable=False)         # 登録を必須にする
    
    # メールアドレス用のフィールド
    email = db.Column(
        db.String,              # String型
        index=True,             # インデックス
        unique=True,            # ユニークキー
        nullable=False)         # 登録を必須にする
    
    # パスワード用のフィールド
    password_hash = db.Column(
        db.String,              # String型
        nullable=False)         # 登録を必須にする
    
    # 投稿日のフィールド
    create_at = db.Column(
        db.DateTime,            # DateTime型
        default=datetime.now)   # 登録時の日時を取得
    
    @property
    def password(self):
        """passwordプロパティの定義
        
        Raises:
            AttributeError: 読み取り不可
        """
        # プロパティが直接参照された場合はAttributeErrorを発生させる
        raise AttributeError('password is not a readable')
    
    @password.setter
    def password(self, password):
        """passwordプロパティのセッター
        
        トップページのビューにおいてフォームに入力されたパスワードを
        passwordプロパティにセットするときに呼ばれる
        
        Args:
            password (str): サインインのフォームで入力されたパスワード
        """
        # ハッシュ化したパスワードをpassword_hashフィールドに格納
        self.password_hash = generate_password_hash(password)

    def is_duplicate_email(self):
        """ユーザー登録時におけるメールアドレスの重複チェックを行う
        
        Returns:
            bool: メールアドレスが重複している場合はTrueを返す
        """
        # データベースから、「emailカラムの内容がサインアップフォームで入力されたメールアドレスと一致するレコードを取得」
        # 該当するレコードが取得された場合はTrueを返し、取得できない場合はFalseを返す
        return User.query.filter_by(email=self.email).first() is not None