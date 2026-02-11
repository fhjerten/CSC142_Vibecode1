class Team:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.players = []
        self.average = None

    def add_player(self, player):
        self.players.append(player)

    def set_team_average(self, stats):
        self.average = stats

    def display_roster(self):
        print(f"\nRoster for {self.name}:")
        for p in sorted(self.players, key=lambda x: x.number):
            print(p)

    def find_player(self, number):
        try:
            number = int(number)
        except:
            return None
        return next((p for p in self.players if p.number == number), None)

    def display_team_average(self):
        if not self.average:
            print("No team averages available.")
            return
        print(f"\nTeam Averages for {self.name}:")
        for stat, value in self.average.items():
            print(f"{stat}: {value}")
