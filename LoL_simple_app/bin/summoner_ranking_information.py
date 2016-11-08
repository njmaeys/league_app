import requests as rq
import riot_api_calls as rac

def get_summoner_tier(tier_raw, summoner_id):
	if summoner_id not in tier_raw:
		return 'Unranked'
	else:
		tier_raw = tier_raw[summoner_id][0]
		tier = tier_raw["tier"].title()
	
		sub_tier_raw = tier_raw["entries"][0]
		sub_tier = sub_tier_raw["division"]
		tier_list = [tier, sub_tier]
		return tier_list

def get_summoner_tier_image(summoner_tier):
	tier_images = 'static/tier_images/'
	return_image = tier_images+summoner_tier.lower()+'.png'
	return return_image

def summoner_tier(summoner_tier_raw):
	if summoner_tier_raw == 'Unranked':
		summoner_tier = ['Unranked', '']
		return summoner_tier
	else:
		summoner_tier = summoner_tier_raw
		return summoner_tier
