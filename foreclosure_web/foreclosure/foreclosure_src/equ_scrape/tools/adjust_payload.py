import json

async def adjust_location(location: str) -> json:
    """
    Function for creating payload that will be used to determine number of records. 
    Takes in location and inserts into pre_total_payload.

    Parameters
    ----------
    location (str): the location that is being searched.

    Returns
    -------
    pre_total_payload (json):  payload that has the location user wants to search.
    """

    pre_total_payload = json.dumps({
      "searchString": location,
      "saleType": [
        "Foreclosure"
      ],
      "autoType": "PLACE"
    })
    return pre_total_payload

async def adjust_payload(location,total_records) -> int:
    """
    Function for creating the finalized payload with location and total records.
    Payload will be used for searching location and extracting the total number of 
    records.

    Parameters
    ----------
    location (str): the location that is being searched.
    total_records (str): the total records associated with the location.

    Returns
    -------
    post_total_payload (json):  payload that has the location and total records to
                                search on equator.com.
    """

    post_total_payload = json.dumps({
        "searchString": location,
        "saleType": [
          "Foreclosure"
        ],
        "autoType": "PLACE",
        "paginationFrom": 0,
        "paginationTo": total_records
      })
    return post_total_payload