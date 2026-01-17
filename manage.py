#!/usr/bin/env python
"""
===============================================
Django Todo アプリ - 管理スクリプト
===============================================

【学習ポイント】
manage.py はDjangoプロジェクトの管理コマンドを実行するためのスクリプト
- python manage.py runserver → 開発サーバー起動
- python manage.py migrate → データベースマイグレーション
- python manage.py createsuperuser → 管理者ユーザー作成
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
