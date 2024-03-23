import requests
import asyncio
import sys 
import os
from .coro_2_get_total_records import equ_get_total_records
from .coro_3_parse_property import parse_property   
from .coro_4_store_data import store_data

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from equ_scrape.tools.headers import equ_headers
from equ_scrape.tools.adjust_payload import adjust_location

async def equ_extract_data(location: str | int) -> None:
    """
    Function for extracting data from the website. 
        * Calls adjust_location and passes in location to update the payload. 
        * Calls equ_get_total_records to find the number of properties associated with that location. 
            Will use finalized payload from equ_get_total_records to request property data. 
        * Calls parse_responses to parse the data.
        * Calls store_data to store the data in PostgresSQL DB.
        * Calls export_to_excel to export the data to a spreadsheet.

    Parameters
    ----------
    location (str | int): the location that the user wants to search. 
                          Could be state, city, or zipcode.

    Returns
    -------
    None

    """
    
    EQUATOR_URL="https://www.equator.com/property/searchproperties"

    location = location
    pre_total_payload = await adjust_location(location)
    post_total_payload = await equ_get_total_records(EQUATOR_URL,location,pre_total_payload)

    responses = requests.request("POST", EQUATOR_URL, headers=equ_headers, data=post_total_payload).json()
    
    parse_property_tasks = [asyncio.create_task(parse_property(response)) for response in responses]
    property_data_fnl = await asyncio.gather(*parse_property_tasks)

    store_property_tasks = [asyncio.create_task(store_data(property_data)) for property_data in property_data_fnl]
    await asyncio.gather(*store_property_tasks)


    return