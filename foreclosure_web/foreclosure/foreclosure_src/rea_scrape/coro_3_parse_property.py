from rea_scrape.tools.combine_details import combine_details

async def rea_parse_property(property_data: dict):
	"""
    Function for processing the provided property data. 
		* Calls combine_details to extract and combine

    Parameters
    ----------
	  property_url (str): url leading to a property on realtor.com. Will be requested.

    Returns
    -------
    property_info_fnl (dict): a dictionary of property data. 
    """

	property_data_fnl = await combine_details(property_data)
	print(property_data_fnl)
	return property_data_fnl
