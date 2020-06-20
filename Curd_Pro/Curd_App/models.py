from django.db import models

class Product_data(models.Model):
	product_id=models.IntegerField()
	product_name=models.CharField(max_length=100)
	product_cost=models.IntegerField()
	product_color=models.CharField(max_length=100)
	product_class=models.CharField(max_length=100)
	custom_name=models.CharField(max_length=100)
	custom_mobile=models.BigIntegerField()
	custom_email=models.EmailField(max_length=100)
	
