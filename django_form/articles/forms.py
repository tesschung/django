from django import forms

# 사용자에게 입력받는 field 작성
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=20)
    content = forms.CharField()
