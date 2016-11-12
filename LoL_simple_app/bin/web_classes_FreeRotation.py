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

		free_list = fcr.get_free_list(data_raw)
		free_champs = fcr.free_champs(free_list)

		return render.free_champions_POST(free_one=free_champs[0],
											free_two=free_champs[1],
											free_three=free_champs[2],
											free_four=free_champs[3],
											free_five=free_champs[4],
											free_six=free_champs[5],
											free_seven=free_champs[6],
											free_eight=free_champs[7],
											free_nine=free_champs[8],
											free_ten=free_champs[9])