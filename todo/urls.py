"""
===============================================
Django Todo アプリ - URLルーティング
===============================================

【学習ポイント: Flask との比較】
- Flask: @app.route("/memos/<int:id>") で個別に定義
- Django: urls.py で一覧化して定義

Flask:
    @app.route("/memos")
    def memo_list(): ...
    
    @app.route("/memos/<int:id>")
    def memo_detail(id): ...

Django:
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/<int:pk>/', views.todo_detail, name='todo_detail'),
"""

from django.urls import path
from . import views

urlpatterns = [
    # ログイン関連（Flask の /login, /logout に相当）
    path('', views.login_view, name='login'),  # ルートはログインページ
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Todo CRUD操作（Flask の /memos 関連に相当）
    # Flask の @app.route("/memos") → path('todos/', ...)
    path('todos/', views.todo_list, name='todo_list'),
    
    # Flask の @app.route("/memos/new") → path('todos/new/', ...)
    path('todos/new/', views.todo_create, name='todo_create'),
    
    # Flask の @app.route("/memos/<int:id>") → path('todos/<int:pk>/', ...)
    path('todos/<int:pk>/', views.todo_detail, name='todo_detail'),
    
    # Flask の @app.route("/memos/<int:id>/edit") → path('todos/<int:pk>/edit/', ...)
    path('todos/<int:pk>/edit/', views.todo_update, name='todo_update'),
    
    # Flask の @app.route("/memos/<int:id>/delete") → path('todos/<int:pk>/delete/', ...)
    path('todos/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
]
