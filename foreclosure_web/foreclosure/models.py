from django.db import models
# from django.contrib.auth.models import User

class EquatorProperties(models.Model):
	source = models.CharField(max_length=25,default='N/A')
	property_url = models.CharField(max_length=500,blank=True)
	street_name = models.CharField(max_length=255,blank=True)
	city = models.CharField(max_length=100,blank=True)
	state = models.CharField(max_length=50,blank=True)
	zip = models.CharField(max_length=10,blank=True)
	county_name = models.CharField(max_length=100,blank=True)
	listed_price = models.CharField(max_length=100,blank=True)
	year_built = models.CharField(max_length=4,blank=True)
	property_type = models.CharField(max_length=50,blank=True)
	description = models.TextField(null=True,blank=True)
	bedroom = models.CharField(max_length=10,blank=True)
	bathroom = models.CharField(max_length=10,blank=True)
	square_ft = models.CharField(max_length=10,blank=True)
	lot_size_sqft = models.CharField(max_length=10,blank=True)
	lot_size_acre = models.CharField(max_length=10,blank=True)
	has_basement = models.CharField(max_length=1,blank=True)
	has_ac = models.CharField(max_length=1,blank=True)
	has_pool = models.CharField(max_length=1,blank=True)
	estimated_cashflow = models.CharField(max_length=10,blank=True)
	estimated_gross_yield = models.CharField(max_length=10,blank=True)
	estimated_net_yield = models.CharField(max_length=10,blank=True)
	mls_number = models.CharField(max_length=20,blank=True)
	realty = models.CharField(max_length=100,blank=True)
	agent_name = models.CharField(max_length=100,blank=True)
	agent_email = models.CharField(max_length=100,blank=True)
	agent_phone = models.CharField(max_length=100,blank=True)
	photo_one = models.CharField(max_length=275,blank=True)
	photo_two = models.CharField(max_length=275,blank=True)
	photo_three = models.CharField(max_length=275,blank=True)
	insert_dt = models.DateTimeField(auto_now_add=True,blank=True)

	def __str__(self):
		return self.source
	

class RealtorProperties(models.Model):
	source = models.CharField(max_length=25,default='N/A')
	property_url = models.CharField(max_length=500,blank=True)
	street_name = models.CharField(max_length=255,blank=True)
	city = models.CharField(max_length=100,blank=True)
	state = models.CharField(max_length=50,blank=True)
	zip = models.CharField(max_length=5,blank=True)
	county_name = models.CharField(max_length=100,blank=True)
	listed_price = models.CharField(max_length=100,blank=True)
	year_built = models.CharField(max_length=4,blank=True)
	property_type = models.CharField(max_length=50,blank=True)
	description = models.TextField(null=True,blank=True)
	bedroom = models.CharField(max_length=10,blank=True)
	bathroom = models.CharField(max_length=10,blank=True)
	square_ft = models.CharField(max_length=10,blank=True)
	stories = models.CharField(max_length=10,blank=True)
	garage = models.CharField(max_length=10,blank=True)
	lot_size_sqft = models.CharField(max_length=10,blank=True)
	monthly_payment = models.CharField(max_length=10,blank=True)
	principal_and_interest = models.CharField(max_length=10,blank=True)
	home_insurance = models.CharField(max_length=10,blank=True)
	hoa_fees = models.CharField(max_length=10,blank=True)
	property_tax = models.CharField(max_length=10,blank=True)
	agent_name = models.CharField(max_length=50,blank=True)
	agent_email = models.CharField(max_length=100,blank=True)
	photo_one = models.CharField(max_length=275,blank=True)
	insert_dt = models.DateTimeField(auto_now_add=True,blank=True)

	def __str__(self):
		return self.source
	

	



