# Django Todo アプリ（学習用・Flask比較）
## 📋 概要（Overview）
このアプリは **Django の基本構造と CRUD 処理**を、Flask の Todo アプリと比較しながら学習するためのサンプルです。
- Django の **URL ルーティング**
- **View（関数ベース）**
- **Session** を使った簡易ログイン
- Todo の **CRUD（作成・一覧・詳細・更新・削除）**
を最小構成で実装しています。
---
## 🎯 想定読者（Who is this for）
- Flask を学習済みで **Django に移行したい人**
- Django の **URL / View / CRUD の関係**が分からない人
- **実務向け README の書き方**を学びたい人
---
## 🛠 使用技術（Tech Stack）
| 技術 | バージョン |
|------|-----------|
| Python | 3.x |
| Django | 4.x |
| SQLite3 | 開発用 |
| HTML | Django Template |
---
## ✨ 機能一覧（Features）
| 機能 | 説明 |
|------|------|
| 🔐 | 簡易ログイン / ログアウト（セッション管理） |
| 📝 | Todo 作成 |
| 📄 | Todo 一覧表示 |
| 🔍 | Todo 詳細表示 |
| ✏️ | Todo 編集 |
| 🗑 | Todo 削除 |
---
## 🔄 画面遷移（Screen Flow）
```
/login
    ↓
/todos/（一覧）
    ├─ /todos/new/（新規作成）
    ├─ /todos/<id>/（詳細）
    │     ├─ /edit/（編集）
    │     └─ /delete/（削除）
    └─ /logout/
```
---
## 🔗 URL設計（Flask との比較）
### Flask の場合
```python
@app.route("/memos")
def memo_list():
    ...
@app.route("/memos/<int:id>")
def memo_detail(id):
    ...
```
### Django の場合（urls.py）
```python
path('todos/', views.todo_list, name='todo_list'),
path('todos/<int:pk>/', views.todo_detail, name='todo_detail'),
```
> 👉 **URL定義を1か所に集約できる**のが Django の特徴
---
## 📁 ディレクトリ構成（抜粋）
```
todo_app/
├─ todo/
│   ├─ views.py        # Flask の route 関数に相当
│   ├─ urls.py         # URL 定義を集約
│   ├─ models.py       # Todo モデル
│   └─ templates/
│       └─ todo/
│           ├─ login.html
│           ├─ todo_list.html
│           ├─ todo_detail.html
│           └─ todo_form.html
```
---
## 🔐 ログイン仕様（簡易版）
> ⚠️ **学習用のため Django 標準認証は使用していません**
- パスワードが `secret` の場合のみログイン成功
- セッションキー `logged_in` で認証状態を管理
```python
request.session['logged_in'] = True
```
Flask の `session["logged_in"] = True` と **ほぼ同じ考え方**です。
---
## 🛡 ログイン制御（Flask風）
Flask の `@login_required` を Django で再現しています。
```python
def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('logged_in'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper
@custom_login_required
def todo_list(request):
    ...
```
> 👉 「**Django = 難しい**」ではなく、考え方は **Flask と同じ**
---
## 📊 CRUD対応表（Flask ⇔ Django）
| 機能 | Flask | Django |
|------|-------|--------|
| 一覧 | `memo_list` | `todo_list` |
| 詳細 | `memo_detail` | `todo_detail` |
| 作成 | `memo_new` | `todo_create` |
| 更新 | `memo_edit` | `todo_update` |
| 削除 | `memo_delete` | `todo_delete` |
---
## 🚀 セットアップ方法
### 1. プロジェクトのクローン
```bash
git clone <repository-url>
cd todo_app
```
### 2. 仮想環境の作成と有効化
```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
```
### 3. 依存パッケージのインストール
```bash
pip install django
```
### 4. データベースのマイグレーション
```bash
python manage.py migrate
```
### 5. 開発サーバーの起動
```bash
python manage.py runserver
```
ブラウザで `http://127.0.0.1:8000/login/` にアクセス
---
## 📝 学習ポイント
### 1️⃣ URL ルーティングの違い
| Flask | Django |
|-------|--------|
| デコレータで分散定義 | `urls.py` に集約 |
| `@app.route("/...")` | `path("...", view)` |
### 2️⃣ View の書き方
| Flask | Django |
|-------|--------|
| `request` はグローバル | `request` は引数で受け取る |
| `return render_template(...)` | `return render(request, ...)` |
### 3️⃣ Session の使い方
```python
# Flask
session['logged_in'] = True
# Django
request.session['logged_in'] = True
```
---
## 📚 参考リンク
- [Django 公式ドキュメント](https://docs.djangoproject.com/)
- [Django Girls チュートリアル](https://tutorial.djangogirls.org/ja/)
---
## 📄 ライセンス
このプロジェクトは学習目的で作成されています。
