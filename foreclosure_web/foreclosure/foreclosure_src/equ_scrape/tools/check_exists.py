async def check_exists(response,key_one, key_two=None, key_three=None):
    
    try: 
        if (key_two != None and key_three == None):
            value = response[f"{key_one}"][f"{key_two}"]

        if key_three != None:
            value = response[f"{key_one}"][key_two][f"{key_three}"]
        
        if key_two == None:
            value = response[f"{key_one}"]
        
    except: value = "N/A" if key_two != "lastName" else ""
    return value


    # try: value = response[f"{key_one}"][f"{key_two}"] if key_two != None else response[f"{key_one}"]
    # except: value = "N/A" if key_two != "lastName" else ""
    # return value