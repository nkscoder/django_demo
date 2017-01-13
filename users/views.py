from django.shortcuts import render


from django.http import HttpResponseRedirect

# Create your views here.
from .models import Profile

def index(request):
    # latest_question_list = Question.objects.order_by('-question_text')[:5]
   return render(request,'index.html')