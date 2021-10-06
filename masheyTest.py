import requests
import json
#import jsonmerge
#from jsonmerge import merge


def asteroid_closest_approach():
    r = requests.get(
        'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1')
    new_json = r.json()
    for i in new_json["near_earth_objects"]:
        closest_distance = i["close_approach_data"][0]["miss_distance"]["miles"]
        cdIndex = 0

        for j in i["close_approach_data"][1:]:
            if j["miss_distance"]["miles"] < closest_distance:
                closest_distance = j["miss_distance"]["miles"]
                cdIndex = i["close_approach_data"].index(j)

        i["close_approach_data"] = [i["close_approach_data"][cdIndex]]

    return(json.dumps(new_json, indent=3, sort_keys=False))


# print(asteroid_closest_approach())


def month_closest_approaches(month, year):
    list_of_jsons = []
    r1 = requests.get(
        'https://api.nasa.gov/neo/rest/v1/feed?start_date={}-{}-01&end_date={}-{}-08&api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1'.format(year, month, year, month))
    new_json1 = r1.json()
    # return(json.dumps(new_json1, indent=3, sort_keys=False))
    for i in new_json1["near_earth_objects"]:
        for d in new_json1["near_earth_objects"][i]:
            closest_distance = d["close_approach_data"][0]["miss_distance"]["miles"]
            cdIndex = 0
            for j in d["close_approach_data"][1:]:
                if j["miss_distance"]["miles"] < closest_distance:
                    closest_distance = j["miss_distance"]["miles"]
                    cdIndex = d["close_approach_data"].index(j)

            d["close_approach_data"] = [d["close_approach_data"][cdIndex]]

    # return(json.dumps(new_json1, indent=3, sort_keys=False))
    list_of_jsons.append(new_json1)

    r2 = requests.get(
        'https://api.nasa.gov/neo/rest/v1/feed?start_date={}-{}-09&end_date={}-{}-16&api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1'.format(year, month, year, month))
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

    r3 = requests.get(
        'https://api.nasa.gov/neo/rest/v1/feed?start_date={}-{}-17&end_date={}-{}-24&api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1'.format(year, month, year, month))
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
    return(json.dumps(list_of_jsons, indent=3, sort_keys=False))


def nearest_misses():
    r = requests.get(
        'https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1')
    new_json = r.json()
    #return(new_json['near_earth_objects'][0]['close_approach_data'][0]['miss_distance']['miles'])
    #return(json.dumps(new_json, indent=3, sort_keys=False))
    for i in new_json["near_earth_objects"]:
        closest_distance = i["close_approach_data"][0]["miss_distance"]["miles"]
        cdIndex = 0

        for j in i["close_approach_data"][1:]:
            if j["miss_distance"]["miles"] < closest_distance:
                closest_distance = j["miss_distance"]["miles"]
                cdIndex = i["close_approach_data"].index(j)

        i["close_approach_data"] = [i["close_approach_data"][cdIndex]]

    new_json.sort(key=lambda x: new_json['near_earth_objects'][0]['close_approach_data'][0]['miss_distance']['miles'])
 #   return(json.dumps(new_json, indent=3, sort_keys=False))
    # Failed approach I thought was good enough to keep for possible adjustments
    #new_json = sorted(new_json, key=_json['near_earth_objects'][0]['close_approach_data'][0]['miss_distance']['miles'])
    #
    # return (json["near_earth_objects"])#['near_earth_objects'])#[0])  #['close_approach_data'][0]['miss_distance']['miles'])
    return(json.dumps(new_json, indent=3, sort_keys=False))


#print(month_closest_approaches('03', '2005'))
print(nearest_misses())
