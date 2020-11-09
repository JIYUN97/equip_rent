from django.shortcuts import render, redirect, get_object_or_404
from .models import RentManage
from managements.forms import RentForm
# Create your views here.

def rent(request):
        if request.method == 'POST':
                # student = Student.objects.get(id=pk)
                rent_form = RentForm(request.POST, request.FILES)
                print(0)
                if rent_form.is_valid():
                        print(55)
                        rent = RentManage()
                        rent.student_id = rent_form.cleaned_data['student_id']
                        rent.name = rent_form.cleaned_data['student_name']
                        rent.phone_number = rent_form.cleaned_data['phone_number']
                        rent.email = rent_form.cleaned_data['email']
                        rent.equip_id = rent_form.cleaned_data ['equip_id']
                        rent.equip_type = rent_form.cleaned_data['equip_type']
                        rent.equip_pic = rent_form.cleaned_data['equip_pic']
                        print(1)
                        rent.save()
                        print(2)
                else:
                        print(10)

                return render(request, 'managements/rent.html', {'rent_form':rent_form} )
        else:
                
                print(4)
                rent_form = RentForm()

                return render(request, 'managements/rent.html', {'rent_form':rent_form})

def main_page(request):
    return render(request, 'managements/main.html',{})