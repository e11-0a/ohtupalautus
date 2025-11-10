class Player:
    def __init__(self, json_dict):
        self.name = json_dict["name"]
        self.team = json_dict["team"]
        self.goals = json_dict["goals"]
        self.assists = json_dict["assists"]
        self.nationality = json_dict["nationality"]

    def julkinen_metodi_jotta_pylint_ei_valite(self):
        return 0

    def __str__(self):
        return self.name
