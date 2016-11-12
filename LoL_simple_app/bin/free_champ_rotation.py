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


def free_champ_images(free_rotation_list):
	free_champ_image_urls = []
	image_url = 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/'

	while len(free_rotation_list) > 0:
		free_name = free_rotation_list.pop(0)
		free_url =	image_url+free_name+'_0.jpg' 	
		free_champ_image_urls.append(free_url)

	return free_champ_image_urls

raw_champ.close()
