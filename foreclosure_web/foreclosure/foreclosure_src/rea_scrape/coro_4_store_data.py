import os
import psycopg2
import string
from dotenv import load_dotenv

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

  load_dotenv()

  conn = psycopg2.connect(
      host = os.getenv("DB_HOST"),
      dbname = os.getenv("DB_NAME"),
      user = os.getenv("DB_USER"),
      password = os.getenv("DB_PASSWORD"),
      port = os.getenv("DB_PORT"),
  )

  cur = conn.cursor()

  cur.execute(f"""
        
      INSERT INTO foreclosure_realtorproperties
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
      stories,
      garage,
      lot_size_sqft,
      monthly_payment,
      principal_and_interest,
      home_insurance,
      hoa_fees,
      property_tax,
      agent_name,
      agent_email,
      photo_one,
      insert_dt
      )
      VALUES
      (
      'REA',
      '{data["Property URL"]}',
      '{data["Street Name"]}',
      '{data["City"]}',
      '{data["State"]}',
      '{data["Zip"]}', 
      '{data["County Name"].replace("'","")}',
      '{data["List Price"]}',
      '{data["Year Built"]}',
      '{string.capwords(data["Property Type"].replace("_"," "))}',
      '{data["Description"].replace('"','').replace("'","") if data["Description"] != None else ""}',
      '{data["Bedroom"]}',
      '{data["Bathroom"]}',
      '{data["Square Feet"]}',
      '{data["Stories"]}',
      '{data["Garage"]}',
      '{data["Lot Size Square Feet"]}',
      '{data["Monthly Payment"]}',
      '{data["Principal & Interest"]}',
      '{data["Home Insurance"]}',
      '{data["HOA Fees"]}',
      '{data["Property Tax"]}',
      '{data["Agent Name"]}',
      '{data["Agent Email"]}',
      '{data["Property Image"]}',
      CURRENT_DATE 
      )
        
      """
  )
  
  conn.commit()
  conn.close()

