# Django Todo アプリ（学習用・Flask比較）

## 概要（Overview）

このアプリは **Django の基本構造と CRUD 処理**を、  
**Flask の Todo アプリと比較しながら学習するためのサンプル**です。

以下の機能を最小構成で実装しています。

- Django の URL ルーティング
- View（関数ベース）
- Session を使った簡易ログイン
- Todo の CRUD（作成・一覧・詳細・更新・削除）

---

## 想定読者（Who is this for）

- Flask を学習済みで Django に移行したい人
- Django の URL / View / CRUD の関係が分からない人
- 実務向け README の書き方を学びたい人

---

## 使用技術（Tech Stack）

- Python 3.x
- Django 4.x
- SQLite3（開発用）
- HTML（Django Template）

---

## 機能一覧（Features）

- 🔐 簡易ログイン / ログアウト（セッション管理）
- 📝 Todo 作成
- 📄 Todo 一覧表示
- 🔍 Todo 詳細表示
- ✏️ Todo 編集
- 🗑 Todo 削除

---

## 画面遷移（Screen Flow）

```text
/login
  ↓
/todos/（一覧）
  ├─ /todos/new/（新規作成）
  ├─ /todos/<id>/（詳細）
  │    ├─ /edit/（編集）
  │    └─ /delete/（削除）
  └─ /logout/
URL設計（Flask との比較）
Flask の場合
python
コードをコピーする
@app.route("/memos")
def memo_list(): ...

@app.route("/memos/<int:id>")
def memo_detail(id): ...
Django の場合（urls.py）
python
コードをコピーする
path('todos/', views.todo_list, name='todo_list'),
path('todos/<int:pk>/', views.todo_detail, name='todo_detail'),
👉 URL定義を1か所に集約できるのが Django の特徴

ディレクトリ構成（抜粋）
text
コードをコピーする
todo_app/
├─ todo/
│  ├─ views.py        # Flask の route 関数に相当
│  ├─ urls.py         # URL 定義を集約
│  ├─ models.py       # Todo モデル
│  └─ templates/
│     └─ todo/
│        ├─ login.html
│        ├─ todo_list.html
│        ├─ todo_detail.html
│        └─ todo_form.html
ログイン仕様（簡易版）
学習用のため Django 標準認証は使用していません

パスワードが secret の場合のみログイン成功

セッションキー logged_in で認証状態を管理

python
コードをコピーする
request.session['logged_in'] = True
Flask の

python
コードをコピーする
session["logged_in"] = True
と ほぼ同じ考え方です。

ログイン制御（Flask風）
Flask の @login_required を Django で再現しています。

python
コードをコピーする
def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('logged_in'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper
python
コードをコピーする
@custom_login_required
def todo_list(request):
    ...
👉 「Django = 難しい」ではなく、考え方は Flask と同じ

CRUD対応表（Flask ⇔ Django）
機能	Flask	Django
一覧	memo_list	todo_list
詳細	memo_detail	todo_detail
作成	memo_new	todo_create
更新	memo_edit	todo_update
削除	memo_delete	todo_delete



 








