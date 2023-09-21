from django.shortcuts import render, HttpResponse
from django.utils import timezone
from random import choice
# from datetime import datetime

# Create your views here.

def index(request):
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6:"Sunday"
    }
    return HttpResponse(f"Hello, world. Today is: {days[timezone.now().weekday()]} {timezone.now().day}/{timezone.now().month}/{timezone.now().year} {timezone.now().time().hour}:{timezone.now().time().minute}:{timezone.now().time().second} <br><a href='dayofweek'>Day Of Week</a><br><a href='cit'>Citations</a><br><a href='multi'>Multiplication scale</a><br><a href='prog_day'>Programer day</a>")

def day_of_the_week(request):
    # Get the current date and time from Django's standard library:
    now = timezone.now().weekday()
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6:"Sunday"
    }
    return HttpResponse(f"Today is {days[now]}")
    # now = datetime.now().day
    # return HttpResponse(now)

def random_citation(request):
    citationList = ["Життя — це те, що з тобою відбувається, поки ти будуєш плани. Джон Леннон",
                    "Прагніть не до успіху, а до цінностей, які він дає. Альберт Айнштайн", 
                    "Найкраща помста — величезний успіх. Френк Сінатра", 
                    "Талант — це дар, якому неможливо ні навчити, ні навчитися. Іммануїл Кант"
                    ]
    return HttpResponse(f"Цитата :  {choice(citationList)}")

def math_scale(request):
    scale = "1 2 3 4 5 6 7 8 9 10<br>2 4 6 8 10 12 14 16 18 20<br>3 6 9 12 15 18 21 24 27 30<br>4 8 12 16 20 24 28 32 36 40<br>5 10 15 20 25 30 35 40 45 50<br>6 12 18 24 30 36 42 48 54 60<br>7 14 21 28 35 42 49 56 63 70<br>8 16 24 32 40 48 56 64 72 80<br>9 18 27 36 45 54 63 72 81 90<br>10 20 30 40 50 60 70 80 90 100"
    return HttpResponse(scale)

def day_256(request):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7:"Sunday"
    }
    year_now = timezone.now().year
    leap_year = year_now % 4
    if leap_year == 0: # IF leap 12 else 13
        time_date = timezone.datetime(day=12, month=9, year=year_now)
    else:
        time_date = timezone.datetime(day=13, month=9, year=year_now)
    first_day = timezone.datetime(day=1, month=1, year=year_now).isoweekday()
    slip = 4 # 256 % 7 == 4
    res = first_day + slip - 1 # IDK why -1 but
    if res > 7:
       res %= 7
    return HttpResponse(f"{days[res]}  {time_date}")
       
    