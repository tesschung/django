from django.contrib import admin
from .models import Article # 동일한 app에 있는 models에서 Article 호출

# Register your models here.
@admin.register(Article)  # admin site에 Article을 register
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')
