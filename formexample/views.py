from django.shortcuts import render
from formexample.forms import formexample
# Create your views here.
def formExample(request):
    form=formexample()
    if request.method == 'POST':
        form = formexample(request.POST)
        if form.is_valid():
            pass
    d1={
        'form':form
    }
    return render(request, 'form.html',d1)