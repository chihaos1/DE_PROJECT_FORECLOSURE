async def create_list(property_list: list):
    """
    Function for creating a list of urls from the provided property list. Extracts
    only the url of the property. 

    Parameters
    ----------
	property_list (list): a list of properties. Contains different data points.

    Returns
    -------
    temp_list (list): a list of property urls. 
    """
    
    temp_list = list()
    temp_list.extend(property["url"] for property in property_list) 
    return temp_list