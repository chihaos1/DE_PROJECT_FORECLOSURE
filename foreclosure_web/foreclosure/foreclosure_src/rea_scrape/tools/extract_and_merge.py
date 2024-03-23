async def extract_and_merge(property_info: dict, to_extract: list, property_url:str) -> dict:
    """
    Function for extracting the needed data from property_info, a dictionary
    that contains data of a property. Uses to_extract to traverse the dictionary
    and locate the needed data. 

    Parameters
    ----------
	property_info (dict): a dictionary of property data.
    to_extract (list): a listed of desired data to extract from property_info. 
    property_url (str): a url to the property.
    Returns
    -------
    merged (dictionary): a dictionary of property data, created by merging the needed
                         parts of data from property_info. 
    """
    
    merged = dict()
    for arg in to_extract:
        if arg == "advertisers":
            merged = merged | {"agent_name": property_info["props"]["pageProps"]["initialReduxState"]["propertyDetails"]["advertisers"][0]["name"],
                               "agent_email": property_info["props"]["pageProps"]["initialReduxState"]["propertyDetails"]["advertisers"][0]["email"]}
        elif arg == "list_price":
            merged = merged | {"listed_price": property_info["props"]["pageProps"]["initialReduxState"]["propertyDetails"][arg]}
        elif arg == "mortgage":
            merged = merged | property_info["props"]["pageProps"]["initialReduxState"]["propertyDetails"]["mortgage"]["estimate"]
        elif arg == "photos":
            merged = merged | {"property_img": property_info["props"]["pageProps"]["initialReduxState"]["propertyDetails"]["photos"][0]["href"].replace("s.jpg","od-w480_h360_x2.webp")}
        else:
            merged = merged | property_info["props"]["pageProps"]["initialReduxState"]["propertyDetails"][arg]
    merged["property_url"] = property_url
    return merged
    
