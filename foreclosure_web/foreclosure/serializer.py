from rest_framework import serializers
from .models import *

class EquatorPropertiesSerializer(serializers.ModelSerializer):
	class Meta:
		model = EquatorProperties
		fields = ["street_name"]
		# fields = ('__all__')
		# fields = ["source","property_url","street_name","city","state","zip",
		# 		  "county_name","listed_price","year_built","property_type",
		# 		  "description","bedroom","bathroom","square_ft","lot_size_sqft",
		# 			"lot_size_acre","has_basement","has_ac","has_pool","estimated_cashflow",
		# 			"estimated_gross_yield","estimated_net_yield","mls_number","realty",
		# 			"agent_name","agent_email","agent_phone","insert_dt"]