import asyncio
from dotenv import load_dotenv
from .equ_scrape.coro_1_extract_data import equ_extract_data
from rea_scrape.rea_main import rea_main
from time import perf_counter
from utils import delete_current_records

async def entrypoint(location: str | int) -> None:
    """
    Function for starting tasks. 

    Parameters
    ----------
    location (str | int): the location that the user wants to search. 
                          Could be state, city, or zipcode.
    """
    t1_start = perf_counter() 
    await delete_current_records()
    # scrape_website_tasks = [asyncio.create_task(equ_extract_data(location)),
    #                         asyncio.create_task(rea_main(location))]
    # await asyncio.gather(*scrape_website_tasks)
    await asyncio.gather(equ_extract_data(location))
    # await asyncio.gather(rea_main(location))
    t1_stop = perf_counter()
    print("Elapsed time:", t1_stop-t1_start) 
    return

def main(location: str | int):
  """
  Function for loading environment variables and calling entrypoint. 

  Parameters
  ----------
	location (str | int): the location that the user wants to search. 
                        Could be state, city, or zipcode.
  """
  load_dotenv()
  asyncio.run(entrypoint(location))

if __name__ == "__main__":
  main()

