"""
===============================================
Django Todo アプリ - ビュー（視点/表示）
===============================================

【学習ポイント: Flask との比較】
- Flask: @app.route() で定義した関数
- Django: views.py でビュー関数/クラスを定義

Flask の各ルート関数がDjangoのビューに相当:
- memo_list() → todo_list()
- memo_new() → todo_create()
- memo_edit() → todo_update()
- memo_delete() → todo_delete()
- memo_detail() → todo_detail()
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Todo


# ----- ログイン処理 -----
# Flask の @app.route("/login", methods=["GET", "POST"]) に相当
def login_view(request):
    """
    【学習ポイント: リクエスト処理】
    - Flask: request.method, request.form["password"]
    - Django: request.method, request.POST.get("password")
    """
    if request.method == 'POST':
        password = request.POST.get('password')
        
        # Flask では password == "secret" でチェックしていた
        # Django でも同様にシンプルな認証を実装
        if password == 'secret':
            # Django の組み込み認証を使う場合は authenticate() を使用
            # ここでは Flask 版に合わせてセッションで管理
            request.session['logged_in'] = True
            return redirect('todo_list')
        else:
            return render(request, 'todo/login.html', {'error': 'パスワードが違います'})
    
    return render(request, 'todo/login.html')


# ----- ログアウト処理 -----
# Flask の @app.route("/logout") に相当
def logout_view(request):
    """
    【学習ポイント: セッションクリア】
    - Flask: session.clear()
    - Django: request.session.flush()
    """
    request.session.flush()
    return redirect('login')


# ----- ログイン必須チェック用デコレータ -----
# Flask の @login_required デコレータに相当
def custom_login_required(view_func):
    """
    Flask版と同じくセッションベースのログインチェック
    """
    def wrapper(request, *args, **kwargs):
        if not request.session.get('logged_in'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


# ----- 一覧表示（Read）-----
# Flask の @app.route("/memos") に相当
@custom_login_required
def todo_list(request):
    """
    【学習ポイント: データ取得】
    - Flask: conn.execute("SELECT * FROM memos ORDER BY created_at DESC").fetchall()
    - Django: Todo.objects.all() （orderingはモデルで定義済み）
    """
    todos = Todo.objects.all()  # SELECT * FROM todo ORDER BY created_at DESC
    return render(request, 'todo/todo_list.html', {'todos': todos})


# ----- 詳細表示（Read - 単一）-----
# Flask の @app.route("/memos/<int:id>") に相当
@custom_login_required
def todo_detail(request, pk):
    """
    【学習ポイント: URLパラメータ】
    - Flask: <int:id> でURLからパラメータを取得
    - Django: urls.py で <int:pk> を定義し、引数で受け取る
    
    get_object_or_404 は指定されたオブジェクトが見つからない場合に404エラーを返す
    Flask の if memo is None: return "メモが見つかりません", 404 に相当
    """
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


# ----- 新規作成（Create）-----
# Flask の @app.route("/memos/new", methods=["GET", "POST"]) に相当
@custom_login_required
def todo_create(request):
    """
    【学習ポイント: フォーム処理とCRUD（Create）】
    - Flask: request.form.get("title"), conn.execute("INSERT...")
    - Django: request.POST.get("title"), Todo.objects.create(...)
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        
        # バリデーション（Flask版と同じ）
        if not title:
            return render(request, 'todo/todo_form.html', {'error': 'タイトルは必須です'})
        
        # Flask の conn.execute("INSERT INTO memos...") に相当
        Todo.objects.create(title=title, content=content)
        
        return redirect('todo_list')
    
    return render(request, 'todo/todo_form.html')


# ----- 編集（Update）-----
# Flask の @app.route("/memos/<int:id>/edit", methods=["GET", "POST"]) に相当
@custom_login_required
def todo_update(request, pk):
    """
    【学習ポイント: CRUD（Update）】
    - Flask: conn.execute("UPDATE memos SET title=?, content=? WHERE id=?")
    - Django: todo.title = new_title; todo.save()
    """
    todo = get_object_or_404(Todo, pk=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        
        if not title:
            return render(request, 'todo/todo_form.html', {
                'todo': todo,
                'error': 'タイトルは必須です'
            })
        
        # Flask の UPDATE 文に相当
        todo.title = title
        todo.content = content
        todo.save()  # これでUPDATEが実行される
        
        return redirect('todo_detail', pk=pk)
    
    return render(request, 'todo/todo_form.html', {'todo': todo})


# ----- 削除（Delete）-----
# Flask の @app.route("/memos/<int:id>/delete", methods=["post"]) に相当
@custom_login_required
def todo_delete(request, pk):
    """
    【学習ポイント: CRUD（Delete）】
    - Flask: conn.execute("DELETE FROM memos WHERE id=?")
    - Django: todo.delete()
    """
    if request.method == 'POST':
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()  # DELETE FROM todo WHERE id = pk
    return redirect('todo_list')
