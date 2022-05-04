from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def say_hello(request):
	return HttpResponse('welcome ')
def home(request):
	print(request)
	return render(request,'home.html')
def ai(request,expn='default expn argument'):
	if expn=='exp1':
		return render(request,'ai/exps/hello.txt')
	else:
		return render(request,'ai/ai.html')
def os(request):
	return render(request,'os/os.html')
def dbms(request):
	return render(request,'dbms/dbms.html')
def r(request):
	return render(request,'r/r.html')