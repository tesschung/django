from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from faker import Faker
import requests
from pprint import pprint
from bs4 import BeautifulSoup

# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name == '': # 이름이 입력되지 않으면 결과페이지로 가지 못하도록 조정
            return render(request, 'jobs/index.html')
        else:
            job = Job.objects.filter(name=name)
            if len(job) == 0: # 이미 DB에 동명이인이 저장되어있어서 queryset이 여러개 들어온다.
                job = Job()
                fake = Faker()
                fake = Faker('ko_KR')
                job.name = name
                job.past_job = fake.job()
                job.save()
                return redirect('jobs:past_job', job.pk)
            else:
                for j in job:
                    return redirect('jobs:past_job', j.pk)
    else: # POST로 들어온 경우가 아니면, index 페이지로만 접근 할 수 있도록 조정
        return render(request, 'jobs/index.html')

# Naver img 사용
def past_job(request, job_pk):
    job = get_object_or_404(Job, pk=job_pk)
    past_job = job.past_job
    url = f'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={past_job}'
    print(url)
    # API는 .json()으로 가능
    response = requests.get(url).text # .json()은 오류, 전달하는 주체가 다르기 때문이다. 
    
    soup = BeautifulSoup(response, 'html.parser')
    soup = soup.find("div", class_="img_area _item")
    imgURL = soup.find("img", class_="_img")
    imgURL = imgURL.get("data-source")
    pprint(imgURL)

    img = imgURL
    
    # pprint(soup)
    context = {
        'job': job,
        'imgURL': imgURL,
        'img' : img
    }
    return render(request, 'jobs/past_job.html', context)
'''
find_all()을 사용하면 img태그를 전부 검색하지만
find()를 사용하면 img태그를 한번만 검색하기 때문에 첫번째 검색
이미지 주소인 src 속성만 빼오면 된다.
그리고 get()함수를 이용해서 'src'속성만 출력한다.
이를 활용하면 해당 링크에 걸린 사진들을 다운로드할 수 있다.
'''


