class Team:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.players = []
        self.average = None

    # add player "object" to the team list
    def add_player(self, player):
        self.players.append(player)

    def set_team_average(self, stats):  # stores all data from the csv file
        self.average = stats

    def display_roster(self): #prints the rosters, by shirt number
        print(f"\nRoster for {self.name}:")
        for p in sorted(self.players, key=lambda x: x.number):
            print(p)

    def find_player(self, number): 
        try:
            number = int(number)
        except:
            return None #stops if user tryes using letters instead of numbers for searching for a player.

        for p in self.players:  # goes through all players, give back the matched one.
            if p.number == number:
                return p

        return None

    # Added too, being able to search player by name.
    def find_player_by_name(self, name):
        for p in self.players:
            if p.name_matches(name):
                return p
        return None

    def display_team_average(self):
        if not self.average:
            print("No team averages available.")
            return

        print(f"\nTeam Averages for {self.name}:")
        for stat, value in self.average.items():
            print(f"{stat}: {value}")