from django.shortcuts import render
import requests
# Create your views here.
def content_list(request): 
    url="https://kmx13dra7a.execute-api.ap-southeast-1.amazonaws.com/Prod/distribute"
    response=requests.get(url)
    data=response.json()
    titles=[]
    links=[]
    for i in data:
        titles.append(i['titles'])
        links.append(i['links'])
    contents=zip(titles,links)
    return render(request,'content_list.html',context={'contents':contents})