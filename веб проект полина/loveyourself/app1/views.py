from django.shortcuts import render

def main_func(request):
    return render(request, 'main.html')
