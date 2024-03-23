import asyncio
from rea_scrape.coro_1_get_property_list import rea_get_property_list
from rea_scrape.coro_2_get_property_details import rea_get_property_details
from rea_scrape.coro_3_parse_property import rea_parse_property
from rea_scrape.coro_4_store_data import store_data

async def rea_main(location: str | int) -> None:
	"""
	Function that controls the flow of rea_scrape. 
	* Calls rea_get_property_list to retrieve a list of urls for foreclosed 
		properties in specified location.
	* Calls rea_get_property_details to retrieve data from each url. 
	* Calls rea_parse_property to extract the needed data points into a dictionary 
		and merge all dictionaries into a list. 
	* Calls export_to_excel to export data into an excel spreadsheet.

	Parameters
	----------
	location (str | int): the location that the user wants to search. 
                          Could be state, city, or zipcode.

	Returns
	-------
	None 
  """

	property_list = await rea_get_property_list(location)
	
	get_property_details_tasks = [asyncio.create_task(rea_get_property_details(property)) for property in property_list]
	property_details = await asyncio.gather(*get_property_details_tasks)
	
	parse_property_details_tasks = [asyncio.create_task(rea_parse_property(property)) for property in property_details]
	property_data_fnl = await asyncio.gather(*parse_property_details_tasks)
	
	store_property_tasks = [asyncio.create_task(store_data(property_data)) for property_data in property_data_fnl]
	await asyncio.gather(*store_property_tasks)

	return
	