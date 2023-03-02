# -*- coding: utf-8 -*-
import requests
import json

# Open states file to read states ID & fetch data from API according to these IDs
file = open('states.json')
# Returns JSON object as a dictionary
states = json.load(file)

jsonfile = []
for state in states:
    # requests.get(...) => send an API request to the link below with a dynamic ID for each state
    # json.loads(response.text) => Parse the response data we get from the API request
    for obj in json.loads(requests.get("https://www.muslima.com/ar/widget/loadcities?stateid=" + str(state['id'])).text):
        dict = {}
        dict['id'] = obj['ATTRIBUTEID']
        dict['name'] = obj['TRANSLATION']
        dict['state'] = state['id']
        jsonfile.append(dict)  
# Always close the file after finishing data process
file.close()

# Write the object into a JSON file
with open("cities.json", "w") as file:
    json.dump(jsonfile, file)