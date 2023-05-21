from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hello, word. You're at the polls index.")
