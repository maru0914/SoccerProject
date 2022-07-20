import json

def get_japanese_team_name(english_team_name):
    with open('data/localize/team_name_list.json', mode='r', encoding='utf-8') as f:
        team_name_dict = json.load(f)
        japanese_team_name = team_name_dict[english_team_name]
    return japanese_team_name
