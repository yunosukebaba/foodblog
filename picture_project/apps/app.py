"""
初期化処理
"""
from flask import Flask

# Flaskのインスタンスを生成
app = Flask(__name__)
# 設定ファイルを読み込む
app.config.from_pyfile('settings.py')

"""トップページのルーティング
"""
from flask import render_template
@app.route('/', methods=['GET', 'POST'])
def index():
    # index.htmlをレンダリングする
    return render_template('index.html')