"""
===============================================
Django Todo アプリ - モデル定義
===============================================

【学習ポイント: Flask との比較】
- Flask: SQL文を直接書いて CREATE TABLE
- Django: モデルクラスを定義し、migrate コマンドで自動作成

Flask での定義:
    CREATE TABLE IF NOT EXISTS memos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

Django では以下のようにクラスで定義する
"""

from django.db import models


class Todo(models.Model):
    """
    Todoモデル（Flask の memos テーブルに相当）
    
    【学習ポイント: Django ORM】
    - id は自動で追加される（AutoField）
    - CharField = TEXT NOT NULL
    - TextField = TEXT (長いテキスト用)
    - DateTimeField = TIMESTAMP
    """
    # Flask の title TEXT NOT NULL に相当
    title = models.CharField(max_length=200, verbose_name='タイトル')
    
    # Flask の content TEXT に相当
    content = models.TextField(blank=True, verbose_name='内容')
    
    # Flask の created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP に相当
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    
    class Meta:
        ordering = ['-created_at']  # Flask の ORDER BY created_at DESC に相当
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
    
    def __str__(self):
        """管理画面などでの表示名"""
        return self.title
