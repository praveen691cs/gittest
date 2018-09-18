from django.shortcuts import render

# Create your views here.
def helloDjango(request):
    name='praveen'
    email='praveenkumar.basireddy@gmail.com'
    dict={'name':name,
    'email':email,
          'l1':[1,2,3,4],
    'dict2':{
        'city':'bangalore',
        'state':'karnataka'
    }
    }
    return render(request, 'hellocompany.html',dict)