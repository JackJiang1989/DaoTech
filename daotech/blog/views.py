from audioop import reverse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import AboutMe, Article, Comment
from django.urls import reverse
from .form import FoodForm, MyForm
# Create your views here.
from datetime import date


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

def article_all(request):
    articles = Article.objects.all()
    context = {'articles': articles}    
    return render(request, 'blog/article_all.html', context)


def article_one(request, article_id):
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
        # print(request.META)
        return render(request, 'blog/article_one.html', context)
    if request.method == 'POST':
        # print(request.POST)
        comment_new = Comment.objects.create(content=request.POST['content'], email=request.POST['email'],article=article)
        # comment_new = Comment(content=request.POST['test'], article=article)
        # comment_new.save()\
        # print(reverse('blog:article_detail', args = (article_id,)))
        # return HttpResponseRedirect(reverse('blog:article_detail', args = (article_id,)))
        return HttpResponseRedirect('/blog/article_one/{article_id}/'.format(article_id = article_id))


def article_archive1(request):
    arch = Article.objects.dates('date', 'month', order = 'DESC')
    archives = {}
    for i in arch:
        pk = i.pk
        year = i.year
        month = i.month
        try:
            archives[year][month-1][1]=True
        except KeyError:
            # catch the KeyError, and set up list for that year
            archives[year]=[[date(year,m,1),False] for m in range(1,13)]
            archives[year][month-1][1]=True
    # print(sorted(archives.items(), reverse=True))
    return render(request, 'blog/article_archive.html', {'archives':sorted(archives.items(), reverse=True)})

def article_archive(request):
    articles = Article.objects.all().order_by('-date')
    archives = {}
    for article in articles:
        # archives.append([article.date.year,article.date,article.title, article.pk])
        try:
            archives[article.date.year].append([article.date,article.title, article.pk])
        except KeyError:
            archives[article.date.year]=[]
            archives[article.date.year].append([article.date,article.title, article.pk])
    # print(archives)
    # print(sorted(archives.items(), key=lambda item:item[0]))
    # test = sorted(archives.items(), key=lambda item:item[0])
    # print(test[0][1][0][0])
    # for a in articles:
    #     print(a.date)
    #     print(a.date.month)
    #     print(a.date.year)      
    #     print(a.title)  
    # context = {'articles': articles}    
    # return HttpResponse('test')
    return render(request, 'blog/article_archive.html', {'archives':sorted(archives.items(), key=lambda item:item[0])})
    # return render(request, 'blog/article_archive.html', {'archives':archives})

def about_me(request):
    about_me = AboutMe.objects.get(pk=1)
    context = {'about_me':about_me}
    return render(request, 'blog/about_me.html', context)


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