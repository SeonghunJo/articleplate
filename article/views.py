from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from newspaper import Article

#/
def index(request):
    context = {}
    return render(request, 'index.html', context)

#/cook/
def cook(request):
    if(request.method == "POST"):
        print("POST")
    else:
        print("GET")
    
    url = request.POST.get('url')
    if(url is None or url == ''):
        return HttpResponseRedirect(article)
    
    article = parse(url, 'ko')
    
    return render(request, 'result.html', {'article':article} )
    #return HttpResponseRedirect('/result', context)

#/article/
def result(request):
    return HttpResponse("Result")
    
#newspaper article parse
def parse(article_url, lang_code):
    article = Article(url = article_url, language = lang_code)
    article.download()
    article.parse()
    
    return article