"""
===============================================
Django Todo アプリ - 設定ファイル
===============================================

【学習ポイント: Flask との比較】
- Flask: app.config で設定
- Django: settings.py で設定を管理

Flask の app.secret_key = "secret" に相当するのが SECRET_KEY
Flask の sqlite3.connect() に相当するのが DATABASES 設定
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Flask の app.secret_key に相当
SECRET_KEY = 'django-insecure-secret-key-for-development'

# SECURITY WARNING: don't run with debug turned on in production!
# Flask の app.run(debug=True) に相当
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
# 【学習ポイント: Djangoはアプリケーション単位で機能を管理】
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',          # 認証機能（Flask のログイン実装に相当）
    'django.contrib.contenttypes',
    'django.contrib.sessions',      # セッション管理（Flask の session に相当）
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo',  # 今回作成するTodoアプリ
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# 【学習ポイント: テンプレート設定】
# Flask の render_template に相当する機能の設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # アプリごとのtemplatesフォルダを使用
        'APP_DIRS': True,  # 各アプリのtemplatesを自動検索
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# 【学習ポイント: データベース設定】
# Flask の sqlite3.connect("unified.db") に相当
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'todo.db',  # Flask の unified.db に相当
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'ja'  # 日本語設定
TIME_ZONE = 'Asia/Tokyo'  # タイムゾーン設定
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 【学習ポイント: ログイン設定】
# Flask では @login_required で手動実装したが、Djangoは組み込み機能
LOGIN_URL = 'login'  # 未ログイン時のリダイレクト先
LOGIN_REDIRECT_URL = 'todo_list'  # ログイン成功後のリダイレクト先
