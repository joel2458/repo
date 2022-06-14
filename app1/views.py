from django.shortcuts import render

# Create your views here.

def group(request):
    return render(request,'group.html')


def base(request):
    return render(request,'base.html')

def load_stock_group(request):
    return render(request,'load_stock_group.html')
    
    
def load_stock_category(request):
    return render(request,'load_stock_category.html')

def load_stock_item(request):
    return render(request,'load_stock_item.html')
