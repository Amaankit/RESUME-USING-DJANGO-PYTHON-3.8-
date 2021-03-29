from django.shortcuts import render

# Create your views here.
def serv(request):
    return render(request,'service/services.html',{'services':'active'})