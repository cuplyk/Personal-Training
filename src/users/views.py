from django.shortcuts import render

# Create your views here.
def login_view(request):
    retur render(request, "authentification/login_page.html")