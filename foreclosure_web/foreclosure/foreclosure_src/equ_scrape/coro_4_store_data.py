import os
import psycopg2

async def store_data(data) -> None:
	"""
	Function for loading scraped data to database on Postgres.

	Parameters
	----------
	data(dict): property values stored in dict for insert

	Returns
	-------
	None
	"""

	conn = psycopg2.connect(host = "foreclosure-db.cq6va2rd6fnp.us-east-1.rds.amazonaws.com",
												dbname = "foreclosure",
												user = "csheng",
												password = "Orientatio135!",
												port = "5432")
	cur = conn.cursor()
			
	cur.execute(
			f"""
			
			INSERT INTO foreclosure_equatorproperties
				(
				source,
				property_url,
				street_name,
				city,
				state,
				zip,
				county_name,
				listed_price,
				year_built,
				property_type,
				description,
				bedroom,
				bathroom,
				square_ft,
				lot_size_sqft,
				lot_size_acre,
				has_basement,
				has_ac,
				has_pool,
				estimated_cashflow,
				estimated_gross_yield,
				estimated_net_yield,
				mls_number,
				realty,
				agent_name,
				agent_email,
				agent_phone,
				photo_one,
				photo_two,
				photo_three,
				insert_dt
				) 
				VALUES
				(
				'EQU',
				'{data["Property URL"]}',
				'{data["Street Name"]}',
				'{data["City"]}',
				'{data["State"]}',
				'{data["Zip"]}',
				'{data["County Name"]}',
				'{data["List Price"]}',
				'{data["Year Built"]}',
				'{data["Property Type"]}',
				'{data["Description"].replace('"','').replace("'","")}',
				'{data["Bedroom"]}',
				'{data["Bathroom"]}',
				'{data["Square Feet"]}',
				'{data["Lot Size Square Feet"]}',
				'{data["Lot Size Square Acre"]}',
				'{data["Has Basement"]}',
				'{data["Has AC"]}',
				'{data["Has Pool"]}',
				'{data["Estimated Cashflow"]}',
				'{data["Estimated Gross Yield"]}',
				'{data["Estimated Net Yield"]}',
				'{data["MLS Number"]}',
				'{data["Realty"].replace('"','').replace("'","")}',
				'{data["Agent Name"].replace('"','').replace("'","")}',
				'{data["Agent Email"]}',
				'{data["Agent Phone"]}',
				'{data["Photo One"]}',
				'{data["Photo Two"]}',
				'{data["Photo Three"]}',
				CURRENT_DATE
					)
		
				"""
	)

	conn.commit()
	conn.close()
