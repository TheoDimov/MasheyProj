import requests
<<<<<<< HEAD

def asteroid_closest_approach():
	r = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1')
	json = r.json()
	for i in json["near_earth_objects"]:
=======
import json 

def asteroid_closest_approach():
	r = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1')
	new_json = r.json()
	for i in new_json["near_earth_objects"]:
>>>>>>> inital commit
		closest_distance = i["close_approach_data"][0]["miss_distance"]["miles"]
		cdIndex = 0

		for j in i["close_approach_data"][1:]:
			if j["miss_distance"]["miles"] < closest_distance:
				closest_distance = j["miss_distance"]["miles"]
				cdIndex = i["close_approach_data"].index(j)
				
<<<<<<< HEAD
		print(i["name"],i["close_approach_data"][cdIndex])
				

#asteroid_closest_approach()

def month_closest_approaches():
	
def nearest_misses():

=======
		i["close_approach_data"] = [i["close_approach_data"][cdIndex]]
	
	return(json.dumps(new_json, indent=3, sort_keys=False))
				

print(asteroid_closest_approach())

def month_closest_approaches():
	r = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-01-01&end_date=2021-01-08&api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1')
	json = r.json()	



def nearest_misses():
	r = requests.get('https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=mpExUO4zavcvnIo4jHS7cLEbf4h0nEyOClIxBif1')
	json = r.json()
	for i in json["near_earth_objects"]:
		closest_distance = i["close_approach_data"][0]["miss_distance"]["miles"]
		cdIndex = 0

		for j in i["close_approach_data"][1:]:
			if j["miss_distance"]["miles"] < closest_distance:
				closest_distance = j["miss_distance"]["miles"]
				cdIndex = i["close_approach_data"].index(j)
				
		print(i["name"],i["close_approach_data"][cdIndex])
>>>>>>> inital commit
	
