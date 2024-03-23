async def combine_details(property_data: dict):
	"""
    Function for combining property details into a dictionary. Calls check_exists
	to ensure value exists in property_data. Combines all property data into property_data_fnl.

    Parameters
    ----------
    property_data (dict): dictionary object that contains details of the property 

    Returns
    -------
    property_data_fnl (dict): dictionary compiled based on selected property details 
    """
	
	property_data_fnl = {
        "Property URL" : await check_exists(property_data,"property_url"),
        "Street Name" : await check_exists(property_data,"address","line"), 
        "City" : await check_exists(property_data,"address","city"), 
        "State" : await check_exists(property_data,"address","state_code"), 
        "Zip" : await check_exists(property_data,"address","postal_code"), 
        "County Name" : await check_exists(property_data,"county","name"), 
        "List Price" : await check_exists(property_data,"listed_price"), 
		"Year Built" : await check_exists(property_data,"year_built"), 
        "Property Type" : await check_exists(property_data,"type"), 
        "Description" : await check_exists(property_data,"text"), 
        "Bedroom" : await check_exists(property_data,"beds"), 
        "Bathroom" : await check_exists(property_data,"baths"), 
        "Square Feet" : await check_exists(property_data,"sqft"),        
        "Stories" : await check_exists(property_data,"stories"), 
        "Garage" : await check_exists(property_data,"garage"), 
        "Lot Size Square Feet" : await check_exists(property_data,"lot_sqft"), 
        "Monthly Payment" : await check_exists(property_data,"monthly_payment"), 
        "Principal & Interest" : await check_exists(property_data, "monthly_payment_details", 0, "amount"), 
        "Home Insurance" : await check_exists(property_data, "monthly_payment_details", 1, "amount"), 
        "HOA Fees" : await check_exists(property_data, "monthly_payment_details", 2, "amount"), 
        "Property Tax" : await check_exists(property_data, "monthly_payment_details", 4, "amount"), 
        "Agent Name" : await check_exists(property_data,"agent_name"), 
        "Agent Email" : await check_exists(property_data,"agent_email"),
        "Property Image" : await check_exists(property_data,"property_img")
		
        }
	return property_data_fnl


async def check_exists(property_data: dict, *args: str|int) -> str:
	"""
    Function for checking if value exists in property_data based on keys. 
	If value does not exist, N/A is returned. 

    Parameters
    ----------
    property_data (dict): dictionary object that contains details of the property 
	args: keys for accessing property_data 

    Returns
    -------
    value (str): the value extracted from property_data
    """
		
	if len(args) == 3:
		try: value = property_data[args[0]][args[1]][args[2]]
		except: value = 'N/A'
	elif len(args) == 2:
		try: value = property_data[args[0]][args[1]]
		except: value = 'N/A'
	elif len(args) == 1:
		try: value = property_data[args[0]]
		except: value = 'N/A'
	return value