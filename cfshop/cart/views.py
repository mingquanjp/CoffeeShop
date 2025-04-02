from django.shortcuts import render

# Create your views here.
def cart_summary(request):
    return render(request,'cart_summary.html',{})


def cart_add(request):
   # return render(request,'cart_add',{})
   pass


def cart_delete(request):
    #return render(request,'cart_delete',{})
    pass

def cart_update(request):
    #return render(request,'cart_update',{})
    pass