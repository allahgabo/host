from django.shortcuts import render
from django.http import HttpResponse
from .models import Product_data
from .forms import Insert_Form,Update_Form,Delete_Form

def home(requset):
	return render(requset,'home.html')

def insert_view(requset):
	if requset.method=='POST':
			form=Insert_Form(requset.POST)
			if form.is_valid():
				product_id=requset.POST.get('product_id','')
				product_name=requset.POST.get('product_name','')
				product_cost=requset.POST.get('product_cost','')
				product_color=requset.POST.get('product_color','')
				product_class=requset.POST.get('product_class','')
				custom_name=requset.POST.get('custom_name','')
				custom_mobile=requset.POST.get('custom_mobile','')
				custom_email=requset.POST.get('custom_email','')
				data=Product_data(
					product_id=product_id,
					product_name=product_name,
					product_cost=product_cost,
					product_color=product_color,
					product_class=product_class,
					custom_name=custom_name,
					custom_mobile=custom_mobile,
					custom_email=custom_email,
					)	
				data.save()
				form=Insert_Form()
				return render(requset,'insert.html',{'form':form})
	else:
		form=Insert_Form()
		return render(requset,'insert.html',{'form':form})
					

def retrive_view(requset):
	product_data=Product_data.objects.all()
	return render(requset,'retrive.html',{'pdata':product_data})

def update_view(requset):
	if requset.method=='POST':
		uform=Update_Form(requset.POST)
		if uform.is_valid():
			product_id=requset.POST.get('product_id','')
			product_cost=requset.POST.get('product_cost','')
			pdata=Product_data.objects.filter(product_id=product_id)
				

			if not pdata:
				return HttpResponse('Product is not Availabe')

			else:
				pdata.update(product_cost=product_cost)
				uform=Update_Form()
				return render(requset,'update.html',{'uform':uform})	
		else:
			return HttpResponse('Invalid Product ID')	
	else:
		uform=Update_Form()
		return render(requset,'update.html',{'uform':uform})			

def delete_view(requset):
	if requset.method=='POST':
		dform=Delete_Form(requset.POST)
		if dform.is_valid():
			product_id=requset.POST.get('product_id','')
			pdata=Product_data.objects.filter(product_id=product_id)

			if not pdata:
				return HttpResponse('Product is not Availabe')
			else:
				pdata.delete()	
				dform=Delete_Form()
				return render(requset,'delete.html',{'dform':dform})	
		else:
			return HttpResponse('Invalid data')
	else:
		dform=Delete_Form()
		return render(requset,'delete.html',{'dform':dform})
							