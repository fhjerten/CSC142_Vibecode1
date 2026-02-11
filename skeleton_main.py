from data_loader import load_teams_from_csv


def main():
    teams = load_teams_from_csv("players1.csv")
    team_list = list(teams.keys())

    print("\nAvailable Teams:")
    for i, (name, gender) in enumerate(team_list, 1):
        print(f"{i}. {name} ({gender})")

    try:
        choice = int(input("Choose team number: ")) - 1
        team = teams[team_list[choice]]
    except:
        print("Invalid selection.")
        return

    team.display_roster()
    team.display_team_average()

    player = team.find_player(input("\nEnter player number: "))
    if player:
        player.display_stats()
    else:
        print("Player not found.")


if __name__ == "__main__":
    main()
