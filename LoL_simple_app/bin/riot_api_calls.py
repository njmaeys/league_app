def get_key(api_key_file):
	with open(api_key_file, 'r') as k:
		key = k.read()
		return key

def summoner_id_url(key, summoner_name):
	summoner_url = ('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/'+summoner_name+'?api_key='+key)
	return summoner_url

def most_played_champions(key, summoner_id):
	most_played_champions = ('https://na.api.pvp.net/championmastery/location/NA1/player/'+summoner_id+'/topchampions?count=5&api_key='+key)
	return most_played_champions

def champion_from_static_aip(key, champ_id):
	champ_name_url = ('https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/'+str(champ_id)+'?champData=image&api_key='+key)
	return champ_name_url

def summoner_tier(key, champ_id):
	champ_ranking_url = ('https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/'+str(champ_id)+'/entry?api_key='+key)
	return champ_ranking_url

def summoner_kda(key, champ_id):
	ranked_data_url = ('https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/'+str(champ_id)+'/ranked?season=SEASON2016&api_key='+key)
	return ranked_data_url

def summoner_ranked_wins_losses(key, champ_id):
	ranked_win_loss_url = ('https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/'+str(champ_id)+'/summary?season=SEASON2016&api_key='+key)
	return ranked_win_loss_url

def recent_match_data(key, champ_id):
	recent_match_data = ('https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/'+str(champ_id)+'/recent?api_key='+key)
	return recent_match_data

def champion_live_data(key):
	champion_url = ('https://na.api.pvp.net/api/lol/na/v1.2/champion?api_key='+key)
	return champion_url