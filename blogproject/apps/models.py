from datetime import datetime
from apps.blogapp import db

class Blogpost(db.Model):
    """
    モデルクラス
    """
    # テーブル名を「posted」にする
    __tablename__ = "posted"

    # 自動的に連番を振るフィールド、プライマリーキー
    id = db.Column(
        db.Integer,             # Integer型
        primary_key=True,       # プライマリーキーに設定
        autoincrement=True)     # 自動連番を振る
    
    # タイトル用のフィールド
    title = db.Column(
        db.String(200),         # String型(最大文字数200)
        nullable=False)         # 登録を必須にする
    
    # 本文用のフィールド
    contents = db.Column(
        db.Text,                # Text型
        nullable=False)         # 登録を必須にする
    
    # 投稿日のフィールド
    create_at = db.Column(
        db.Date,                # Date型
        default=datetime.today())     # 現在の日付を取得