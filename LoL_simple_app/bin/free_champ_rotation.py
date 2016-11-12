import riot_api_calls as rac
import requests as rq
import helper_functions as hf
import json


key_file = hf.get_key_file()
key = rac.get_key(key_file)

champ_file = 'templates/champions.json' 

raw_champ = open(champ_file)
champ_data = json.load(raw_champ)

def get_champ_name(champ_id):
    new_data = champ_data["data"]
    for k, v in new_data.iteritems():
        ids = str(v.values()[1])
        if ids == champ_id:
            return v.values()[3]

def get_free_list(data):
	free_list = []
	champ_data = data["champions"]
	for i in champ_data:
		if i.values()[4] == True:
			free_list.append(i.values()[5])

	return free_list

def free_champs(free_list):
	free_champions = []
	while len(free_list) > 0:
		for i in free_list:
			champ_id = free_list.pop(0)
			free_names = get_champ_name(str(champ_id))
			free_champions.append(free_names)

	return free_champions

raw_champ.close()
