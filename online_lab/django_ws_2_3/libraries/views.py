from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    import requests
    API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = 'ttbchacmanz1920001'
    params = {
        'ttbkey': API_KEY,
        'QueryType' : 'ItemNewSpecial',
        'MaxResults' : 50,
        'SearchTarget' : 'Book',
        'Output' : 'JS',
        'Version' : 20131101,
    }

    response = requests.get(API_URL,params=params).json()
    # print(response['item'])

    # ctrl + shift + `

    result = []
    for item in response['item']:
        info = {
            '제목' : item['title'],
            '저자' : item['author'],
            '출간일' : item['pubDate'],
            '국제 표준 도서 번호' : item['isbn'],
        }
        #print(info)
        result.append(info)
        
    context = {
        'result' : result,
    }

    return render(request, 'recommend.html',context)