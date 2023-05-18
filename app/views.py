from django.shortcuts import render
from app.forms import*
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
#FBV for returning string
def fbv_string(request):
    return HttpResponse('this fbv  string')

#cbv for returning string
class cbv_string(View):
    def get(self,request):
        return HttpResponse('this is cbv string')
#fbv for returning html page
def fbv_html(request):
    return render(request,'fbv_html.html')

class cbv_html(View):
    def get(self, request):
        return render(request,'cbv_html.html')
#Handling forms by using fbv
def fbv_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')
    return render(request,'fbv_form.html',d) 

#Handling forms by using cbv
class cbv_form(View):
    def get(self, request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'cbv_form.html',d)


    def post(self, request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')


















