from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from newspaper import Article

from article.models import Plate

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
    #if(url is None or url == ''):
    #    return HttpResponseRedirect(article)
    
    article = parse(url, 'ko')
    insertDatabase(article)
    
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

def insertDatabase(article):
    doc = Plate(url=article.url)
    if(article.title is not None):
        doc.title = article.title
    if(article.text is not None):
        doc.text = article.text
    if(article.top_image is not None):
        doc.top_image = article.top_image
    if(article.images is not None):
        doc.images = article.images
    
    doc.save()
    return