from django.shortcuts import render
from django.http import HttpResponse , JsonResponse


# Create your views here.

def home(request):
    context={
        'name': 'arash',
        'age': 25,
        'job':'programmer' 
    }
    context ={
        'articles':
        [
            {
                'title': 'برد ۶ گله حریف آسیایی پرسپولیس',
                'descriptions':'به گزارش "ورزش سه"، در یکی از مسابقات هفته پانزدهم ویسشایا لیگا تاجیکستان، تیم فوتبال استقلال دوشنبه که حریف پرسپولیس ایران در لیگ قهرمانان آسیا است، از ساعت ۲۰ یکشنبه شب مقابل تیم رده ششمی خالتون قرار گرفت.',
                'img':'https://static.farakav.com/files/pictures/thumb/01602762.jpg'
            },
            {
                'title': 'حمایت از لیونل مسی روی سکوهای نوکمپ (عکس)',
                'descriptions':'به گزارش "ورزش سه"، 20348 هوادار حاضر در نوکمپ پیش از بازی بارسا برابر سوسیداد و نیز در جریان بازی با سر دادن شعارهایی به حمایت از لیونل مسی اسطوره خود پرداختند.',
                'img':'https://static2.farakav.com/files/pictures/01634654.jpg'
            },
            {
                'title': 'شگفت‌انگیز است؛ از پیوستن‌ به قهرمان‌ایتالیا خوشحالم',
                'descriptions':'استفان دی فرای دوست من است و ما از یک شهر هستیم. من او را خیلی خوب می شناسم و خوشحالم که اینجاست و با یکدیگر هم تیمی هستیم. ',
                'img':'https://static2.farakav.com/files/pictures/01634457.jpg'
            },
        ]
    }
    return render(request , "blog/home.html" , context ) 



# def home(request):
#     return HttpResponse ('welcome to webloot')
# ------------------------------------------------------------------
# def api(request):
#     return JsonResponse ({'title':'سلام'}