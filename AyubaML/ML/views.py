from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_choice(request):
    return render(request,'get_choice.html')

def asset_opt_in(request):
    return render(request,'opt_in.html')