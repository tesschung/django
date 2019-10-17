from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = '__all__'
        # exclude로 article을 제외하고 하도록 하거나,
        # fields = ['content'] 이처럼 받고싶은 field만 가져와서 정의할 수 있다.
        exclude = ['article']