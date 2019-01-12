from django.shortcuts import render

# Create your views here.
def landing_page(request):
    if not request.user.is_authenticated:
        return render(request,'welcome.html')