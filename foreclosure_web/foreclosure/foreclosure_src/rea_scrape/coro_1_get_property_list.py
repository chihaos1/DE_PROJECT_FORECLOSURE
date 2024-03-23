import json
import httpx
import random
import asyncio
import string
import selectolax
from rea_scrape.tools.headers import rea_headers_properties
from rea_scrape.tools.create_list import create_list

async def rea_get_property_list(location: str | int):
    """
    Function for retrieving data of foreclosed properties from realtor.com in 
    a specified location. Parsed using selectolax and loaded into a dictionary. 
        * Calls create_list to extract url of the properties and aggregate results
            into a list. 

    Parameters
    ----------
    location (str | int): the location that the user wants to search. 
                          Could be state, city, or zipcode.

    Returns
    -------
    property_list (list): a list of property urls. 
    """
    
    async with httpx.AsyncClient() as client:
        
        search_link = f"https://www.realtor.com/realestateandhomes-search/{string.capwords(location)}/show-foreclosure"
        print(search_link)
        response = await client.request("GET", search_link, headers=rea_headers_properties, timeout=10.0)
        print(response)
        response_parsed = selectolax.parser.HTMLParser(response.text)
        properties_json = json.loads(response_parsed.css_first("[data-testid='seoLinkingData']").text())
        property_list = await create_list(properties_json[0]["mainEntity"]['itemListElement']) #stored in this key.
        return property_list


    