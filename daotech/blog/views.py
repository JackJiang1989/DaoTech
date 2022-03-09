from audioop import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Article, Comment
from django.urls import reverse
from .form import FoodForm, MyForm
# Create your views here.

def index(request):
    articles = Article.objects.all()
    for_highlight = Article.objects.get(pk=1)
    for_card1 = Article.objects.get(pk=2)
    for_card2 = Article.objects.get(pk=3)
    context = {'articles': articles,
                'for_highlight': for_highlight,
                'for_card1': for_card1,
                'for_card2': for_card2}
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
        print(request.META)
        return render(request, 'blog/article_detail.html', context)
    if request.method == 'POST':
        print(request.POST)
        comment_new = Comment.objects.create(content=request.POST['content'], email=request.POST['email'],article=article)
        # comment_new = Comment(content=request.POST['test'], article=article)
        # comment_new.save()\
        # print(reverse('blog:article_detail', args = (article_id,)))
        # return HttpResponseRedirect(reverse('blog:article_detail', args = (article_id,)))
        return HttpResponseRedirect('/blog/article_detail/{article_id}/'.format(article_id = article_id))



def markdowntest(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            normal = form.cleaned_data['content_normal']
            markdown = form.cleaned_data['content_markdown']
            context = {
            'normal': normal,
            'markdown': markdown
            }
            return HttpResponse(normal + markdown)
    else:
        form = MyForm()
    context = {'form':form}
    return render(request, 'blog/form.html', context)




def food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        # print(form.is_bound)
        if form.is_valid:
            form.save()
            # alternatively:
            # my_model = form.save(commit=False)  # create model, but don't save to database
            # my.model.something = whatever  # if I need to do something before saving it
            # my.model.save()            

    else:
        form = FoodForm()
    # print(form.is_bound)
    context = {'form':form}
    return render(request, 'blog/food.html', context)