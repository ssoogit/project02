from django.shortcuts import render

def mainpage(request) :
    return render(request, 'mpage/mainpage.html')

def service(request) :
    return render(request, 'mpage/serv.html')

def information(request) :
    return render(request, 'mpage/info.html')

def seatpage(request) :
    return render(request, 'mpage/seat.html')

def loginpage(request) :
    return render(request, 'mpage/login.html')

def joinpage(request) :
    return render(request, 'mpage/join.html')
from django.shortcuts import render

# Create your views here.
