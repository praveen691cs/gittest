from django.shortcuts import render, redirect
from crud.forms import EmployeeForm
from crud.models import Employee

# Create your views here.
def create(request):
    form=EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp=Employee()
            empname = form.cleaned_data['emp_email'].split('@')[0]
            emp.emp_name = empname
            emp.emp_email = form.cleaned_data['emp_email']
            emp.address = form.cleaned_data['address']
            emp.phone = form.cleaned_data['phone']
            emp.save()
            return redirect(index)
    return  render(request,'crud/create.html',{'form':form})

def index(request):

    resultset= Employee.objects.all()
    return render(request,'crud/index.html',{'data':resultset})

def update(request,id):

    data = Employee.objects.get(id=id)
    form = EmployeeForm(instance=data)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            emp = Employee()
            emp.id=id
            empname = form.cleaned_data['emp_email'].split('@')[0]
            emp.emp_name = empname
            emp.emp_email = form.cleaned_data['emp_email']
            emp.address = form.cleaned_data['address']
            emp.phone = form.cleaned_data['phone']
            emp.save()
            return redirect(index)
    return render(request, 'crud/update.html', {'form': form})



def delete(request,id):
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect(index)

def view(request,id):
    data = Employee.objects.get(id=id)
    return render(request,'crud/view.html',{'data':data})


