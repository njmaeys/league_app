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
											free_eleven=free_champs[10],
											free_twelve=free_champs[11],
											free_thirteen=free_champs[12],
											free_fourteen=free_champs[13],
											free_fifteen=free_champs[14],
											free_sixteen=free_champs[15],
											free_seventeen=free_champs[16],
											free_eighteen=free_champs[17],
											free_nineteen=free_champs[18],
											free_twenty=free_champs[19],
											image_one="".join((image_url+free_image_list[0]+'_0.jpg').split()),
											image_two="".join((image_url+free_image_list[1]+'_0.jpg').split()),
											image_three="".join((image_url+free_image_list[2]+'_0.jpg').split()),
											image_four="".join((image_url+free_image_list[3]+'_0.jpg').split()),
											image_five="".join((image_url+free_image_list[4]+'_0.jpg').split()),
											image_six="".join((image_url+free_image_list[5]+'_0.jpg').split()),
											image_seven="".join((image_url+free_image_list[6]+'_0.jpg').split()),
											image_eight="".join((image_url+free_image_list[7]+'_0.jpg').split()),
											image_nine="".join((image_url+free_image_list[8]+'_0.jpg').split()),
											image_ten="".join((image_url+free_image_list[9]+'_0.jpg').split()),
											image_eleven="".join((image_url+free_image_list[10]+'_0.jpg').split()),
											image_twelve="".join((image_url+free_image_list[11]+'_0.jpg').split()),
											image_thirteen="".join((image_url+free_image_list[12]+'_0.jpg').split()),
											image_fourteen="".join((image_url+free_image_list[13]+'_0.jpg').split()),
											image_fifteen="".join((image_url+free_image_list[14]+'_0.jpg').split()),
											image_sixteen="".join((image_url+free_image_list[15]+'_0.jpg').split()),
											image_seventeen="".join((image_url+free_image_list[16]+'_0.jpg').split()),
											image_eighteen="".join((image_url+free_image_list[17]+'_0.jpg').split()),
											image_nineteen="".join((image_url+free_image_list[18]+'_0.jpg').split()),
											image_twenty="".join((image_url+free_image_list[19]+'_0.jpg').split()))