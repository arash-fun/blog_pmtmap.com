# paginator
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse , JsonResponse
from .models import Article, Category 


# Create your views here.

def home(request , page=1 ):
    articles_list = Article.objects.published()
    paginator = Paginator(articles_list , 4)
    # page = request.GET.get('page')
    articles = paginator.get_page(page)

    # context={
    #     'name': 'arash',
    #     'age': 25,
    #     'job':'programmer' 
    # }
    # # context ={
    #     'articles':
    #     [
    #         {
    #             'title': 'برد ۶ گله حریف آسیایی پرسپولیس',
    #             'descriptions':'به گزارش "ورزش سه"، در یکی از مسابقات هفته پانزدهم ویسشایا لیگا تاجیکستان، تیم فوتبال استقلال دوشنبه که حریف پرسپولیس ایران در لیگ قهرمانان آسیا است، از ساعت ۲۰ یکشنبه شب مقابل تیم رده ششمی خالتون قرار گرفت.',
    #             'img':'https://static.farakav.com/files/pictures/thumb/01602762.jpg'
    #         },
    #         {
    #             'title': 'حمایت از لیونل مسی روی سکوهای نوکمپ (عکس)',
    #             'descriptions':'به گزارش "ورزش سه"، 20348 هوادار حاضر در نوکمپ پیش از بازی بارسا برابر سوسیداد و نیز در جریان بازی با سر دادن شعارهایی به حمایت از لیونل مسی اسطوره خود پرداختند.',
    #             'img':'https://static2.farakav.com/files/pictures/01634654.jpg'
    #         },
    #         {
    #             'title': 'شگفت‌انگیز است؛ از پیوستن‌ به قهرمان‌ایتالیا خوشحالم',
    #             'descriptions':'استفان دی فرای دوست من است و ما از یک شهر هستیم. من او را خیلی خوب می شناسم و خوشحالم که اینجاست و با یکدیگر هم تیمی هستیم. ',
    #             'img':'https://static2.farakav.com/files/pictures/01634457.jpg'
    #         },
    #     ]
    # }

    context ={
        # use manager instead of status = ...
        # 'articles':Article.objects.filter(status = 'p') ,
        # 'articles':Article.objects.published(),
        'articles':articles,

        # category added for show in home page
        # 'category':Category.objects.filter(status=True)
    }
    return render(request , "blog/home.html" , context ) 

def detail_article(request , slug ):
    context = {
        # 'article':Article.objects.get(slug = slug)
        # use manager instead of status = ...
        # 'article':get_object_or_404(Article , slug = slug , status = 'p'),

        'article':get_object_or_404(Article.objects.published() , slug = slug ),

        # 'category':Category.objects.filter(status=True)
    }
    return render (request , 'blog/detail_article.html' , context)


def category(request,slug ,page =1):
    category = get_object_or_404(Category , slug = slug , status =True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list , 4)
    articles = paginator.get_page(page)

    context = {

        'category': category,
        'articles':articles

    }
    return render (request , 'blog/category.html' , context)







# def home(request):
#     return HttpResponse ('welcome to webloot')
# ------------------------------------------------------------------
# def api(request):
#     return JsonResponse ({'title':'سلام'}