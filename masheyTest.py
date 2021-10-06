# Name: Theo Dimov
# Proj: Asteroid Hunter v1.1.0

import requests
import json
import operator

# This function returns in JSON the closest approach per astroid in the NASA browse API. 

def asteroid_closest_approach():
    # Simple request to the API and initalization a JSON object.
    r = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1')
    new_json = r.json()
    
    # Loop through JSON each asteroid and find closest distance then equate it's closest approach data to the
    # single closet approach
    for i in new_json["near_earth_objects"]:
        closest_distance = i["close_approach_data"][0]["miss_distance"]["miles"]
        cdIndex = 0

        for j in i["close_approach_data"][1:]:
            if j["miss_distance"]["miles"] < closest_distance:
                closest_distance = j["miss_distance"]["miles"]
                cdIndex = i["close_approach_data"].index(j)

        i["close_approach_data"] = [i["close_approach_data"][cdIndex]]

    # Return JSON in proper structure
    return(json.dumps(new_json, indent=3, sort_keys=False))



# Function returns the closest approaches per asteroid in a specificed month of a year.

def month_closest_approaches(month, year): 
    #Initalize list later for merging and JSON object through API request representing the first week of the month    
    list_of_jsons = []
    r1 = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date={}-{}-01&end_date={}-{}-08&api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1'.format(year, month, year, month))
    new_json1 = r1.json()


    # Loop through each day and find closest approach for every asteroid during that day of the week  
    for i in new_json1["near_earth_objects"]:
        for d in new_json1["near_earth_objects"][i]:
            closest_distance = d["close_approach_data"][0]["miss_distance"]["miles"]
            cdIndex = 0
            for j in d["close_approach_data"][1:]:
                if j["miss_distance"]["miles"] < closest_distance:
                    closest_distance = j["miss_distance"]["miles"]
                    cdIndex = d["close_approach_data"].index(j)

            d["close_approach_data"] = [d["close_approach_data"][cdIndex]]
    
    # Add weekly JSON to list	
    list_of_jsons.append(new_json1)

    #Same operation for 2nd week of the month
    r2 = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date={}-{}-09&end_date={}-{}-16&api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1'.format(year, month, year, month))
    new_json2 = r2.json()

    for i in new_json2["near_earth_objects"]:
        for d in new_json2["near_earth_objects"][i]:
            closest_distance = d["close_approach_data"][0]["miss_distance"]["miles"]
            cdIndex = 0
            for j in d["close_approach_data"][1:]:
                if j["miss_distance"]["miles"] < closest_distance:
                    closest_distance = j["miss_distance"]["miles"]
                    cdIndex = d["close_approach_data"].index(j)

            d["close_approach_data"] = [d["close_approach_data"][cdIndex]]

    list_of_jsons.append(new_json2)

    #Third week operation
    r3 = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date={}-{}-17&end_date={}-{}-24&api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1'.format(year, month, year, month))
    new_json3 = r3.json()

    for i in new_json3["near_earth_objects"]:
        for d in new_json3["near_earth_objects"][i]:
            closest_distance = d["close_approach_data"][0]["miss_distance"]["miles"]
            cdIndex = 0
            for j in d["close_approach_data"][1:]:
                if j["miss_distance"]["miles"] < closest_distance:
                    closest_distance = j["miss_distance"]["miles"]
                    cdIndex = d["close_approach_data"].index(j)

            d["close_approach_data"] = [d["close_approach_data"][cdIndex]]

    list_of_jsons.append(new_json3)

    # Nest cases in conditionals depending on month type ie: 30 day, 31 day or Feb.
    # This way the last week can be properaly accounted for.
    if int(month) % 2 != 0:
        r4 = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date={}-{}-25&end_date={}-{}-30&api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1'.format(year, month, year, month))
    elif int(month) == 2:
        r4 = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date={}-{}-25&end_date={}-{}-28&api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1'.format(year, month, year, month))
    else:
        r4 = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date={}-{}-25&end_date={}-{}-31&api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1'.format(year, month, year, month))
    
    new_json4 = r4.json()

    for i in new_json4["near_earth_objects"]:
        for d in new_json4["near_earth_objects"][i]:
            closest_distance = d["close_approach_data"][0]["miss_distance"]["miles"]
            cdIndex = 0
            for j in d["close_approach_data"][1:]:
                if j["miss_distance"]["miles"] < closest_distance:
                    closest_distance = j["miss_distance"]["miles"]
                    cdIndex = d["close_approach_data"].index(j)

            d["close_approach_data"] = [d["close_approach_data"][cdIndex]]

    list_of_jsons.append(new_json4)

    # Merge through a json.dump function. The shortcoming in this was the seperate element counts not totalized in the end
    # But certainly can be with an improved merger
    return(json.dumps(list_of_jsons, indent=3, sort_keys=False))

# The last function collected 10 closest misses from the browse API. Not completed yet, biggest obstacle is the sorting of the JSON by
# distance which was not yet successfully completed by sort, sorted, including lambda functions.

def nearest_misses():
    # Could simply call asteroid_closest_approach() function and skip this section but was working with making sure the JSON 
    # object was still comfortable to work with for me not one that's been dumped and a more organized structure
    r = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1')
    new_json = r.json()
    
    for i in new_json["near_earth_objects"]:
        closest_distance = i["close_approach_data"][0]["miss_distance"]["miles"]
        cdIndex = 0

        for j in i["close_approach_data"][1:]:
            if j["miss_distance"]["miles"] < closest_distance:
                closest_distance = j["miss_distance"]["miles"]
                cdIndex = i["close_approach_data"].index(j)

        i["close_approach_data"] = [i["close_approach_data"][cdIndex]]

    # Portion of attempts made at sorting, indices don't match when placed in lambda functions. Dict not accepted in sort function and
    # string indicies not accepted in sorted function

    #new_json = json.loads(new_json)   
    #new_json.sort(key=lambda x: x['near_earth_objects'][0]['close_approach_data'][0]['miss_distance']['miles'])
    #new_json = sorted(new_json, key=lambda k: k[1][0])#[2][0])#'near_earth_objects'])#[0]['close_approach_data'][0]['miss_distance']['miles'])#['close_approach_data'][0]['miss_distance']['miles'])
    
    return(json.dumps(new_json, indent=3, sort_keys=False))


#Function Test Runs
#print(asteroid_closest_approach())
#print(month_closest_approaches('03', '2005'))
#print(nearest_misses())
