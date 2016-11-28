import web
import requests as rq
import riot_api_calls as rac
import summoner_simple_data as ssd
import top5_most_played_champs as t5
import summoner_ranking_information as sri
import helper_functions as hf
import web_classes_SummonerProfile as SP
import web_classes_Index as IX
import web_classes_FreeRotation as FR
import os

urls = (
	'/', 'Index',
	'/summoner_profile', 'SummonerProfile',
	'/summoner_profile/no_summoner_found', 'noSummoner',
	'/free_rotation', 'FreeRotation'
	)

app = web.application(urls, globals())

# Call the web_class files to help keep this script cleaner
# Each url can be defined in a web_class file and called here in the urls
SummonerProfile = SP.SummonerProfile
Index = IX.Index
FreeRotation = FR.FreeRotation


if __name__ == "__main__":
	app.run()
