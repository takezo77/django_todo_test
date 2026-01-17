"""
Django Admin設定
管理画面でTodoを管理できるようにする（Django独自の機能）
"""
from django.contrib import admin
from .models import Todo

admin.site.register(Todo)
