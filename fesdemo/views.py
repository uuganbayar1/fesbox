from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 

# Create your views here.
# static
def Home(req):
    return render(req, 'index.html')