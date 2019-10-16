from django import forms
from .models import Article
# 받아서 검증하고 저장한다.
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
