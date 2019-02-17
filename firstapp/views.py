from django.shortcuts import render
from .forms import UserForm
from django.template.loader import get_template
#from django.template import Context
import datetime
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
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
    return render(request, "firstapp/current_datetime.html", {"current_date": test2})

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})


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


'''
def products(request, productid= 21):
    output = "<h2>Product № {0}</h2>".format(productid)
    return HttpResponse(output)


def users(request, id=777, name="Default-User"):
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)

'''