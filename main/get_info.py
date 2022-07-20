from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import tz
import json
import locale
import pprint
import requests

# try scraping  
def get_match_info_by_scraping():
    target_url = 'https://www.espn.com/soccer/team/fixtures/_/id/103/ita.ac_milan'
    html_text = requests.get(target_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    with open('sample_output.txt', 'w', encoding='utf-8') as f:
        f.write(str(soup))


def get_match_info_by_api():
    target_url = 'https://api.football-data.org/v4/teams/98/matches'
    with open('data/temp/football_data_api_token.txt') as f:
        access_token = f.read().strip()

    headers = {"X-Auth-Token" : access_token}
    r_get = requests.get(target_url, headers=headers)
    print(r_get.status_code)
    pprint.pprint(r_get.json())
    with open('sample.json', 'w') as f:
        json.dump(r_get.json(), f, indent=4)
    
def test_get_info_from_json():
    locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
    return_list = []
    JST = tz.gettz('Asia/Tokyo')
    UTC = tz.gettz("UTC")
    with open('sample.json', mode='r', encoding='utf-8') as f:
        input_dict = json.load(f)
        for match in input_dict['matches']:
            utctime = datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=UTC).astimezone(JST)
            output_time = utctime.strftime('%Y-%m-%d %H:%M (%a)')
            tmp_dict = {}
            tmp_dict['schedule'] = output_time
            tmp_dict['home_name'] = match['homeTeam']['name']
            tmp_dict['away_name'] = match['awayTeam']['name']
            return_list.append(tmp_dict)
    return return_list



