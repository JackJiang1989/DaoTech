from audioop import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Comment, MarkDownTest
from django.urls import reverse
from .form import MyForm
# Create your views here.

def index(request):
    articles = Article.objects.all()
#    articles = Article.objects.filter()
    context = {'articles': articles}
    return render(request, 'blog/index.html', context)
#    return HttpResponse("hello world")


def article_detail(request, article_id):
    #get the parameter from URL #article1
 #   article = Article.objects.filter(id = id)
#    article = Article.objects.get(pk = id)
    article = get_object_or_404(Article, pk=article_id)
    # comment = get_object_or_404(Comment, article = article)
    try:
        comments = Comment.objects.filter(article = article)
    except Comment.DoesNotExist:
        comments = None
    context = {'article': article, 'comments':comments}
    if request.method == 'GET':
        return render(request, 'blog/article_detail.html', context)
    if request.method == 'POST':
        comment_new = Comment.objects.create(content=request.POST['content'], email=request.POST['email'],article=article)
        # comment_new = Comment(content=request.POST['test'], article=article)
        # comment_new.save()\
        # print(reverse('blog:article_detail', args = (article_id,)))
        # return HttpResponseRedirect(reverse('blog:article_detail', args = (article_id,)))
        return HttpResponseRedirect('/blog/article_detail/{article_id}/'.format(article_id = article_id))



def markdowntest(request):
    MDT = MarkDownTest()
    context = {'MDT': MDT}
    return render(request, 'blog/form.html', context)
