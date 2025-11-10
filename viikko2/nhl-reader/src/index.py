import sys

from rich.console import Console
from rich.table import Table

import requests
from player import Player

console = Console()


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def julkinen_metodi_jotta_pylint_ei_valite(self):
        return 0

    def get_players(self) -> list[Player]:
        response = requests.get(self.url, timeout=90)
        if response.status_code != 200:
            sys.exit(1)
        response = response.json()
        players = []
        for player_dict in response:
            players.append(Player(player_dict))
        return players


class PlayerStats:
    def __init__(self, other) -> None:
        self.players: list[Player] = other.get_players()

    def julkinen_metodi_jotta_pylint_ei_valite(self):
        return 0

    def top_scorers_by_nationality(self, nationality):
        return sorted(filter(lambda x: x.nationality == nationality, self.players), key=lambda x: x.goals+x.assists, reverse=True)


def main():
    kausi = input("Kausi (esim. 2024-25): ")  # "2024-25"
    url = f"https://studies.cs.helsinki.fi/nhlstats/{kausi}/players"
    while True:
        kansalaisuus = input("Kansalaisuus (esim. FIN): ")
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(kansalaisuus)

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Nimi")
        table.add_column("Joukkue")
        table.add_column("Maalit")
        table.add_column("Assists")
        table.add_column("Yhteensä")
        for i in players:
            table.add_row(
                i.name,
                i.team,
                f"{i.goals}",
                f"{i.assists}",
                f"{i.goals+i.assists}"
            )
        console.print(table)


if __name__ == "__main__":
    main()
