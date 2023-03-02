# -*- coding: utf-8 -*-
import requests
import json

jsonfile = []
id = 1

while json.loads(requests.get("https://www.muslima.com/ar/widget/loadstates?countryid=" + str(id)).text):
    for obj in json.loads(requests.get("https://www.muslima.com/ar/widget/loadstates?countryid=" + str(id)).text):
        dict = {}
        dict['id'] = obj['ATTRIBUTEID']
        dict['name'] = obj['TRANSLATION']
        dict['country'] = id
        jsonfile.append(dict)
    id += 1

with open("states.json", mode="w", encoding="utf-8") as file:
    json.dump(jsonfile, file)
