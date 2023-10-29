from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#what ever we do in this function below is going to be assigned to empty quotation in the url,i just kept pass there because nothing for now
"""
def index(request):
    pass
"""
#lets do an example of what i explained in the previous paragraph. and we have to do httpresponse from django too
#another thing that can be done is creating a dictionary with variables that can be used in index.html file . 
# #remember to add the name of the dictionary to the return render

def index(request):

    context = {
        'name': 'patrick',
        'age' : 23,
        'nationality': 'British',
    }
    return render(request, 'index.html', context)

def counter(request):
    text = request.POST['text']
    amount_of_word = len(text.split())
    return render(request,'counter.html', {'amount': amount_of_word})