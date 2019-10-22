from django import forms
from .models import Article, Comment
# 받아서 검증하고 저장한다.
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        # form에서 user을 exclude하여 자동으로 해당 유저로만 접근해서 저장하도록 한다.
        exclude = ['user', ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]
        # exclude = ['article', ]