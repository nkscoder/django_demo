from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
# def index(request):
#     return HttpResponse("Hello, You are at the core index.")
#
#
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
#
# from .models import Question
from django.template import loader
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = '<br>'.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


# def index(request):
#     latest_question_list = Question.objects.order_by('-question_text')[:5]
#     # template = ('core/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request,'index.html', context)
#

# def login(request):
#
#     return render(request,'login.html')

# def register(request):
#     return render(request,'register.html')
#
#
# def registerPost(request):
#     return render(request,'login.html')

from .forms import LoginForm

# def login(request):
#     username = "not logged in "
#     if request.method == "POST":
#         MyLoginForm = LoginForm(request.POST)
#         if MyLoginForm.is_valid():
#             username = MyLoginForm.cleaned_data['username']
#
#         else:
#             MyLoginForm = LoginForm()
#
#     return render(request,'login.html',{"username":username})

def login(request):
    username = "not logged in "
    form = LoginForm()
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']

        else:
            MyLoginForm = LoginForm()

    return render(request,'login.html',{"username":username, 'form':form})