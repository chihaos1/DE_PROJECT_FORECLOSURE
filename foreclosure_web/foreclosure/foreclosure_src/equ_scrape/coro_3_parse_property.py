import os
import sys 

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from equ_scrape.tools.check_exists import check_exists
# from equ_scrape.coro_4_store_data import store_data

async def parse_property(response: dict) -> None:
    """
    Function for parsing property values. Calls check_exists to verify
    if value exists. Stores all values in a dictionary and returns.

    Parameters
    ----------
    response (dict): Dictionary object that contains property key-value pairs. 

    Returns
    -------
    None
    """

    data = {
        "Property URL" : f"www.equator.com/pdp/propertyId/{await check_exists(response,'propertyId')}", 
        "Street Name" : await check_exists(response,"address","address1"), 
        "City" : await check_exists(response,"address","city"), 
        "State" : await check_exists(response,"address","state"), 
        "Zip" : await check_exists(response,"address","zip"), 
        "County Name" : await check_exists(response,"address","countyName"), 
        "Year Built" : await check_exists(response,"additionalDetails","yearBuilt"), 
        "List Price" : await check_exists(response,"details","listPrice"), 
        "Price Change" : await check_exists(response,"details","priceChange"), 
        "Property Type" : await check_exists(response,"details","propertyType"), 
        "Description" : await check_exists(response,"details","description"), 
        "Bedroom" : await check_exists(response,"details","bedroom"), 
        "Bathroom" : await check_exists(response,"details","bath"), 
        "Square Feet" : await check_exists(response,"details","squareFeet"),        
        "Has Basement" : "Y" if await check_exists(response,"additionalDetails","hasBasement") == 1 else "N", 
        "Has AC" : "Y" if await check_exists(response,"additionalDetails","hasAc") == 1 else "N", 
        "Has Pool" : "Y" if await check_exists(response,"additionalDetails","hasPool") == 1 else "N", 
        "Lot Size Square Feet" : await check_exists(response,"additionalDetails","lotSizeSqft"), 
        "Lot Size Square Acre" : await check_exists(response,"additionalDetails","lotSizeAcre"), 
        "Estimated Cashflow" : await check_exists(response,"cashFlow"), 
        "Estimated Gross Yield" : await check_exists(response,"grossYield"), 
        "Estimated Net Yield" : await check_exists(response,"netYield"), 
        "MLS Number" : await check_exists(response,"mlsNumber"), 
        "Realty" : await check_exists(response,"agent","companyName"),  
        "Agent Name" : await check_exists(response,"agent","firstName") + " " + await check_exists(response,"agent","lastName") , 
        "Agent Email" : await check_exists(response,"agent","email"), 
        "Agent Phone" : await check_exists(response,"agent","workPhone"), 
        "Photo One": f"https://www.equator.com/768x512/{await check_exists(response,'propertyId')}/{await check_exists(response,'photos', 0, 'filename')}" if await check_exists(response,'photos', 0, 'filename') != 'N/A' else "N/A" ,
        "Photo Two": f"https://www.equator.com/768x512/{await check_exists(response,'propertyId')}/{await check_exists(response,'photos', 1, 'filename')}" if await check_exists(response,'photos', 1, 'filename') != 'N/A' else "N/A" ,
        "Photo Three": f"https://www.equator.com/768x512/{await check_exists(response,'propertyId')}/{await check_exists(response,'photos', 2, 'filename')}" if await check_exists(response,'photos', 2, 'filename') != 'N/A' else "N/A" 
    }
    
    return data