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

class SummonerProfile:
	def GET(self):
		summoner_response = ""
		return render.summoner_profile_form(summoner_response=summoner_response)

	def POST(self):
		form = web.input(summoner="nobody")
		summoner = "%s" % (form.summonerProfile)

		raw_summoner = rq.get(rac.summoner_id_url(key, summoner))
		if str(raw_summoner) == "<Response [404]>":
			summoner_response =  "Summoner Not Found Try Again"
			return render.summoner_profile_form(summoner_response=summoner_response)
		else:
			summoner_raw = raw_summoner.json()

			summoner_access = ssd.get_summoner_access(summoner_raw)
			summoner_level = ssd.get_summoner_level(summoner_access, summoner_raw)

			summoner_id = ssd.get_summoner_id(summoner_access, summoner_raw)
			summoner_icon = ssd.get_summoner_icon(summoner_access, summoner_raw)

			# Most Played Champion Data
			most_played_url = rac.most_played_champions(key, summoner_id)
			raw_most_played_champs = rq.get(most_played_url)
			most_played_raw_data = raw_most_played_champs.json()

			most_played_champ_list = t5.most_played_list(key, most_played_raw_data)
			most_played_list = t5.most_played_name(most_played_champ_list)
			most_played_image_list = t5.most_played_image(most_played_champ_list)
			most_played_title_list = t5.most_played_title(most_played_champ_list)

			# Current Tier and Sub Ranking
			raw_tier = rq.get(rac.summoner_tier(key, summoner_id))
			tier_raw = raw_tier.json()

			summoner_tier_raw = sri.get_summoner_tier(tier_raw, summoner_id)
			summoner_tier = sri.summoner_tier(summoner_tier_raw)

			tier_image = sri.get_summoner_tier_image(summoner_tier[0])

			# Summoner K/D/A
			kda_raw = rq.get(rac.summoner_kda(key, summoner_id)).json()
			kda_list = ssd.get_kda(kda_raw)
			wins_losses_raw = rq.get(rac.summoner_ranked_wins_losses(key, summoner_id)).json()
			win_lose_list = ssd.get_win_lost(kda_list, wins_losses_raw)

			average_kda_list = ssd.calc_average_kda(kda_list, win_lose_list)

			# Most winning champion
			most_winning_raw = rq.get(rac.recent_match_data(key, summoner_id)).json()
			most_winning_id = t5.current_most_winning_champ(most_winning_raw)
			most_winning_name_raw = rq.get(rac.champion_from_static_aip(key, most_winning_id)).json()
			most_winning_name = t5.single_champ_name(most_winning_name_raw)

			return render.summoner_profile_POST(summoner_name=summoner_access,
											summoner_level=summoner_level,
											champ_one=most_played_list[0],
											champ_two=most_played_list[1],
											champ_three=most_played_list[2],
											champ_four=most_played_list[3],
											champ_five=most_played_list[4],
											image_one=most_played_image_list[0],
											image_two=most_played_image_list[1],
											image_three=most_played_image_list[2],
											image_four=most_played_image_list[3],
											image_five=most_played_image_list[4],
											title_one=most_played_title_list[0],
											title_two=most_played_title_list[1],
											title_three=most_played_title_list[2],
											title_four=most_played_title_list[3],
											title_five=most_played_title_list[4],
											most_played_champ=most_played_image_list[5],
											summoner_icon=summoner_icon,
											summoner_tier=summoner_tier[0],
											summoner_sub_tier=summoner_tier[1],
											tier_image=tier_image,
											ranked_wins=win_lose_list[0],
											ranked_losses=win_lose_list[1],
											average_kills=average_kda_list[0],
											average_deaths=average_kda_list[1],
											average_assists=average_kda_list[2],
											most_winning_champion=most_winning_name)