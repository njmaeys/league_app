import json 


def get_summoner_access(summoner_data):
	for i in summoner_data:
		access_name = i
		return access_name

def get_summoner_level(access_name, summoner_data):
	summoner_level = summoner_data[access_name]["summonerLevel"]
	return str(summoner_level)

def get_summoner_id(access_name, summoner_data):
	summoner_id = summoner_data[access_name]["id"]
	return str(summoner_id)

def get_summoner_icon(access_name, summoner_data):
	summoner_icon_url = 'http://ddragon.leagueoflegends.com/cdn/6.21.1/img/profileicon/'
	summoner_icon = summoner_data[access_name]["profileIconId"]
	summoner_icon_image = summoner_icon_url+str(summoner_icon)+'.png'
	return summoner_icon_image

# Summoner Stats
def get_kda(ranked_data):
	kda_list = []
	try:
		if ranked_data["champions"]:
			ranked_stats = ranked_data["champions"]
			for stats in ranked_stats:
				if stats["id"] == 0:
					kills = stats["stats"]["totalChampionKills"]
					deaths = stats["stats"]["totalDeathsPerSession"]
					assists = stats["stats"]["totalAssists"]
					kda_list.append(kills)
					kda_list.append(deaths)
					kda_list.append(assists)
	except KeyError, e:
		kda_list.append(0)
		kda_list.append(0)
		kda_list.append(0)

	return kda_list

def get_win_lost(kda_list, wins_losses):
	if sum(kda_list) == 0:
		wins_losses_list = [0,0]
		return wins_losses_list
	else:
		wins_losses_list = []
		wl_data = wins_losses["playerStatSummaries"]
		for wl in wl_data:
			if wl["playerStatSummaryType"] == 'RankedSolo5x5':
				wins = wl["wins"]
				losses = wl["losses"]
				wins_losses_list.append(wins)
				wins_losses_list.append(losses)

		return wins_losses_list

def calc_average_kda(kda_list, win_loss_list):
	if sum(win_loss_list) == 0:
		average_kda = [0,0,0]
		return average_kda
	else:
		average_kda = []
		kill = kda_list[0]
		death = kda_list[1]
		assist = kda_list[2]

		wins = win_loss_list[0]
		losses = win_loss_list[1]
		total_games = wins + losses

		average_kills = kill / total_games
		average_deaths = death / total_games
		average_assists = assist / total_games

		average_kda.append(average_kills)
		average_kda.append(average_deaths)
		average_kda.append(average_assists)

		return average_kda
