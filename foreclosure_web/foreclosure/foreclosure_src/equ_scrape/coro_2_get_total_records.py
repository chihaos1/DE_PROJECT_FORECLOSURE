import requests
import os
import sys 

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from equ_scrape.tools.headers import equ_headers
from equ_scrape.tools.adjust_payload import adjust_payload

async def equ_get_total_records(url,location,pre_total_payload) -> dict:
    """
    Function for getting total records from a specific location. Calls adjust_payload
    and passes in total_records to finalized payload. Total records will determine
    how many properties to receive from the website through XHR.

    Parameters
    ----------
    url (str): the link to the website.
    location (str): the location that is being searched.
    pre_total_payload (json): payload that has the location but not the 
                              total records to request. 

    Returns
    -------
    post_total_payload (json): payload that has the location and total record counts. 
                               Will be used in request to website 
    """
    
    responses = requests.request("POST", url, headers=equ_headers, data=pre_total_payload).json()
    print(len(responses))
    total_records = responses[0]["totalRecords"] if len(responses) != 0 else 0
    post_total_payload = await adjust_payload(location,total_records)
    return post_total_payload
