import asyncio
import httpx
import json
import selectolax
import random

from rea_scrape.tools.headers import rea_headers_property
from rea_scrape.tools.extract_and_merge import extract_and_merge

async def rea_get_property_details(property_url:str) -> dict:
    """
    Function for retrieving data of individual property from realtor.com and
    returning property data in a dictionary. Sends request using httpx and parses
    with selectolax. to_extract contains the parts of data that are desired.
    	* Calls extract_and_merge to extract the needed data segments from a dictionary
    		and merge into a dictionary.

    Parameters
    ----------
	property_url (str): url leading to a property on realtor.com. Will be requested.

    Returns
    -------
    property_info_fnl (dict): a dictionary of property data. 
    """

    async with httpx.AsyncClient() as client:
      wait_sec = random.randint(1,5)
      await asyncio.sleep(wait_sec)
      response = await client.request("GET", property_url, headers=rea_headers_property)
      response_parsed = selectolax.parser.HTMLParser(response.text)
      property_info = json.loads(response_parsed.css_first("[id='__NEXT_DATA__']").text())
      to_extract = ["location", "description", "list_price", "advertisers", "mortgage", "photos"]
      property_info_fnl = await extract_and_merge(property_info, to_extract, property_url)
      return property_info_fnl    
    # Could add estimates, schools, environment, etc...