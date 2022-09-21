import http.client
import datetime
import json

def get_Data(req_date):
	conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

	headers = {
	    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
	    'x-rapidapi-key': "*****************************"
	    }

	conn.request("GET", f"/games?date={req_date}", headers=headers)

	res = conn.getresponse()
	data = res.read()
	res_json = json.loads(data.decode("utf-8"))

	if res_json["response"]:
		game_list = res_json["response"]
		for i in range(len(game_list)):
			try:
				teams = game_list[i]["teams"]
				visitor = teams["visitors"]["name"]
				host = teams["home"]["name"]
				if visitor == "Minnesota Timberwolves" or host == "Minnesota Timberwolves":
					print(f"{req_date}")
					break
			except KeyError:
				print(f"Exception on {req_date}")
				break
	else:
		print(f"No game on {req_date}")

today = datetime.date.today()
for date_diff in range(0, 8):
	req_date = today + datetime.timedelta(days=date_diff)
	get_Data(str(req_date))
