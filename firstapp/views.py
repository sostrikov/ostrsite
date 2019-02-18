from django.shortcuts import render
from .forms import UserForm
from django.template.loader import get_template
#from django.template import Context
import datetime
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template import Context, Template
from django.utils import timezone
from django.utils.timezone import localtime, get_current_timezone, datetime
import pytz


# Create your views here. {"form": userform},
tz = localtime()
from django.shortcuts import render_to_response
import pytz
# Create your views here.
'''
def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
'''
def current_datetime(request):
    now = datetime.datetime.now()
    test2 = pytz.timezone('Europe/Moscow').localize( now )
    formatedDate = test2.strftime("%Y-%m-%d %H:%M:%S")
    return render(request, "firstapp/current_datetime.html", {"current_date": now})

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        userform = UserForm()
        header = "Обычная переменная"  # обычная переменная
        langs = ["English", "German", "Spanish"]  # массив
        user = {"name": "Вася Куралесов", "age": 23}  # словарь
        addr = ("Абрикосовая", 23, 45)  # кортеж

        data = {"header": header, "langs": langs, "user": user, "address": addr}
        #data = {"header": "Hello Django", "message": "Welcome to Python"}
        return render(request, "index.html", context=data)

def parse_timestamp(n):
    naive = datetime.datetime.fromtimestamp(int(n))
    # FIXME: what timezone is it really?
    from django.utils import timezone
    tz = timezone.get_current_timezone()
    local = tz.localize(naive)
    return local

#def index(request):
    #return render(request, "index.html")


def about(request):
    return HttpResponse("<h2>О сайте</h2>")


def contact2(request):
    return HttpResponse("<h2>Контакты</h2>")


def details(request):
    return HttpResponseRedirect("/")


def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Product № {0}  Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)

def main(request):

    t = Template('No TZ activated, now is {{ n1 }}, str: {{ n1_str }} <br>')
    n1 = timezone.now()
    args = {"n1": n1.strftime("%a %d-%m-%Y %H:%M:%S %z"),
            "n1_str": str(n1)}
    resp = t.render(Context(args))

    timezone.activate(pytz.timezone("Europe/Moscow"))
    n2 = timezone.now()
    args["n2"] = n2.strftime("%a %d-%m-%Y %H:%M:%S %z")
    args["n2_str"] = str(n2)
    t = Template('Moscow TZ activated, now is {{ n2 }}, str: {{ n2_str }}')
    resp += t.render(Context(args))

    return HttpResponse(resp)

'''
def products(request, productid= 21):
    output = "<h2>Product № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id=777, name="Default-User"):
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)

'''