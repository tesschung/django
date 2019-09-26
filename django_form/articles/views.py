from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 모든 article을 보여주는 페이지
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

# GET으로 들어오면 생성하는 페이지 rendering
# POST로 들어오면 생성하는 로직 수행
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): # (유효성 검사) 사용자가 입력한 데이터가 model에 정의한 것에 맞춰 유효한 데이터인가?
            title = form.cleaned_data.get('title') # 유효한 데이터를 꺼낸다
            content = form.cleaned_data.get('content')
            # title = request.POST.get('title')
            # content = request.POST.get('content')
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:index')
        # else: # form 이 not valid한 경우 따로 처리를 해야 한다.
        #     context = {
        #         'form':form}
        #     return render(request, 'articles/create.html', context)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)