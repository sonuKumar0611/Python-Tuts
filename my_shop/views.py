from django.shortcuts import render

# Create your views here.
def show_my_shop(request):
    return render(request, "shop_home.html")