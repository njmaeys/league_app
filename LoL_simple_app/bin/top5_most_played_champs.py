import requests as rq
import riot_api_calls as rac

def most_played_list(my_key, most_played_data):
	most_played_list = []
	for item in most_played_data:
		champ_ids = item["championId"]
		most_played_list.append(champ_ids)

	most_played_by_name = []  
	while len(most_played_list) > 0:
		champ_id = most_played_list.pop(0)
		call = rq.get(rac.champion_from_static_aip(my_key, champ_id))
		data = call.json()
		champ_name = data["name"]
		champ_image = data["image"]["full"]
		champ_title = data["title"]

		most_played_by_name.append((champ_name, champ_image, champ_title))

	return most_played_by_name 

def most_played_name(most_played_list):
	most_played_name = [x[0] for x in most_played_list]
	champ_one = most_played_name[0]
	champ_two = most_played_name[1]
	champ_three = most_played_name[2]
	champ_four = most_played_name[3]
	champ_five = most_played_name[4]
	name_list = [champ_one, champ_two, champ_three, champ_four, champ_five]

	return name_list

def most_played_image(most_played_list):
	image_url = 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/'
	most_played = 'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'

	most_played_image = [x[1] for x in most_played_list]
	image_one = image_url+((most_played_image[0].rstrip('png')).rstrip('.'))+'_0.jpg'
	image_two = image_url+((most_played_image[1].rstrip('png')).rstrip('.')).rstrip('.')+'_0.jpg'
	image_three = image_url+((most_played_image[2].rstrip('png')).rstrip('.'))+'_0.jpg'
	image_four = image_url+((most_played_image[3].rstrip('png')).rstrip('.'))+'_0.jpg'
	image_five = image_url+((most_played_image[4].rstrip('png')).rstrip('.'))+'_0.jpg'

	most_played_champ_url = most_played+((most_played_image[0].rstrip('png')).rstrip('.'))+'_0.jpg'
	image_list = [image_one, image_two, image_three, image_four, image_five, most_played_champ_url]
	return image_list

def most_played_title(most_played_list):
	most_played_title = [x[2] for x in most_played_list]
	title_one = most_played_title[0].title()
	title_two = most_played_title[1].title()
	title_three = most_played_title[2].title()
	title_four = most_played_title[3].title()
	title_five = most_played_title[4].title()

	title_list = [title_one, title_two, title_three, title_four, title_five]
	return title_list

# Current most winning champion
def current_most_winning_champ(match_data):
	recent_games = []

	champ_data = match_data["games"]
	for match in champ_data:
		champ_id = match["championId"]
		win_loss = match["stats"]["win"]
		recent_win_loss =  (champ_id, win_loss)

		if recent_win_loss[1] == True:
			recent_games.append(recent_win_loss)

	most_winning_champ_id = max(set(recent_games), key=recent_games.count)[0]
	return most_winning_champ_id

def single_champ_name(champ_data):
	champ_name = champ_data["name"]
	return champ_name