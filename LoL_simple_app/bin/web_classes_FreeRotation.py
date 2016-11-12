import web
import requests as rq
import riot_api_calls as rac
import summoner_simple_data as ssd
import top5_most_played_champs as t5
import summoner_ranking_information as sri
import helper_functions as hf
import free_champ_rotation as fcr
import os


key_file = hf.get_key_file()
key = rac.get_key(key_file)

render = web.template.render('templates/')

class FreeRotation:
	def GET(self):
		data = rq.get(rac.champion_live_data(key))
		data_raw = data.json()

		image_url = 'http://ddragon.leagueoflegends.com/cdn/img/champion/loading/'

		free_list = fcr.get_free_list(data_raw)
		free_champs = fcr.free_champs(free_list)
		free_image_list = free_champs

		return render.free_champions_POST(free_one=free_champs[0],
											free_two=free_champs[1],
											free_three=free_champs[2],
											free_four=free_champs[3],
											free_five=free_champs[4],
											free_six=free_champs[5],
											free_seven=free_champs[6],
											free_eight=free_champs[7],
											free_nine=free_champs[8],
											free_ten=free_champs[9],
											image_one=image_url+free_image_list[0]+'_0.jpg',
											image_two=image_url+free_image_list[1]+'_0.jpg',
											image_three=image_url+free_image_list[2]+'_0.jpg',
											image_four=image_url+free_image_list[3]+'_0.jpg',
											image_five=image_url+free_image_list[4]+'_0.jpg',
											image_six=image_url+free_image_list[5]+'_0.jpg',
											image_seven=image_url+free_image_list[6]+'_0.jpg',
											image_eight=image_url+free_image_list[7]+'_0.jpg',
											image_nine=image_url+free_image_list[8]+'_0.jpg',
											image_ten=image_url+free_image_list[9]+'_0.jpg')