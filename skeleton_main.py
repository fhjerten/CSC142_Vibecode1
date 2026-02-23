from data_loader import load_teams_from_csv


def select_team(teams):
    team_list = list(teams.keys())

    print("\nAvailable Teams:")
    for i, (name, gender) in enumerate(team_list, 1):
        print(f"{i}. {name} ({gender})")

    try:
        return teams[team_list[int(input("Choose team number: ")) - 1]]
    except:
        print("Invalid selection.")
        return None


def view_player_stats(team): # number or name for search
    choice = input("\nSearch by (1) number or (2) name: ")

    if choice == "1":  # if search number
        player = team.find_player(input("Enter player number: "))
    elif choice == "2":  # if search name
        player = team.find_player_by_name(input("Enter player name: "))
    else:
        print("Invalid choice.")
        return

    if player:  # if player found, prints stats.
        player.display_stats()
    else:
        print("Player not found.")


# The meny for ONE SELECTED TEAM
def team_menu(team):
    while True:
        print(f"\n===== {team.name} =====")
        print("1. View roster\n2. View team average\n3. View player stats\n4. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            team.display_roster()
        elif choice == "2":
            team.display_team_average()
        elif choice == "3":
            view_player_stats(team)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

# Starting menu, for the whole program when running at start
def main():
    teams = load_teams_from_csv("players1.csv")

    while True:
        print("\n===== Albright Basketball Stats =====")
        print("1. Select team\n2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            team = select_team(teams)
            if team:
                team_menu(team)
        elif choice == "2":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()