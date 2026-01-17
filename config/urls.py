"""
===============================================
Django Todo アプリ - メインURL設定
===============================================

【学習ポイント: Flask との比較】
- Flask: @app.route("/memos") でルーティング
- Django: urls.py でルーティングを一元管理

Flask では各関数に @app.route() を付けるが、
Django では urls.py にすべてのURLパターンを定義する
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 管理画面（Django独自の機能）
    path('admin/', admin.site.urls),
    
    # todoアプリのURLを読み込み
    # Flask の app.py に直接書くのと違い、アプリごとにURLを分離
    path('', include('todo.urls')),
]
