import csv
from player import Player
from team import Team


def load_teams_from_csv(filename):
    teams = {}  #the starting dictionary for teams

    with open(filename, encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:

            if not row or not row[0].strip():  #doesnt read the rows in the csv with no team name
                continue

            team_name, gender, number, name = row[:4]
            key = (team_name.strip(), gender.strip())

            if key not in teams:
                teams[key] = Team(*key)

            stats = dict(zip(
                ["PPG", "FGA", "FG%", "3PT%", "FT%", "AST", "STL", "BLK"], # the selected stats displayed
                row[4:12]
            ))

            if number.strip() == "":
                teams[key].set_team_average(stats)
            else:
                teams[key].add_player(
                    Player(team_name, gender, number, name, stats)
                )

    return teams