from datetime import datetime
from dateutil import tz
import json
import locale
import requests

from utils import localize


def get_team_list(league_code):

    with open(f'data/info_from_api/team_list_{league_code}.json', mode='r', encoding='utf-8') as f:
        return json.load(f)

def get_match_list(league_code, team_id):
    locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
    match_list = []
    JST = tz.gettz('Asia/Tokyo')
    UTC = tz.gettz("UTC")
    with open(f'data/info_from_api/match_list_{league_code}.json', mode='r', encoding='utf-8') as f:
        input_dict = json.load(f)
        for match in input_dict['matches']:
            if team_id in (match['homeTeam']['id'], match['awayTeam']['id']):
                utc_match_date = datetime.strptime(match['utcDate'], '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=UTC).astimezone(JST)
                output_date = utc_match_date.strftime('%Y-%m-%d %H:%M (%a)')
                match_info = {}
                match_info['schedule'] = output_date
                match_info['home_name'] = localize.get_japanese_team_name(match['homeTeam']['name']) if league_code == 'SA' else match['homeTeam']['name']
                match_info['away_name'] = localize.get_japanese_team_name(match['awayTeam']['name']) if league_code == 'SA' else match['awayTeam']['name']
                match_info['home_logo'] = match['homeTeam']['crest']
                match_info['away_logo'] = match['awayTeam']['crest']
                match_list.append(match_info)
    return match_list

def get_team_name_from_id(league_code, team_id):
    with open(f'data/info_from_api/team_list_{league_code}.json', mode='r', encoding='utf-8') as f:
        input_dict = json.load(f)
        for team in input_dict['teams']:
            if team_id == team['id']:
                return team['name']

