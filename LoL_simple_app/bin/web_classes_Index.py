import web
import requests as rq
import riot_api_calls as rac
import summoner_simple_data as ssd
import top5_most_played_champs as t5
import summoner_ranking_information as sri
import helper_functions as hf
import os


key_file = hf.get_key_file()
key = rac.get_key(key_file)

render = web.template.render('templates/')

class Index:
	def GET(self):
		return render.index_template()