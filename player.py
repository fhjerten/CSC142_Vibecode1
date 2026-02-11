class Player:
    def __init__(self, team, gender, number, name, stats):
        self.team = team
        self.gender = gender
        self.number = int(number)
        self.name = name
        self.stats = stats

    def __str__(self):
        return f"{self.number} {self.name}"

    def display_stats(self):
        print(f"\nStats for {self.name} (#{self.number})")
        for stat, value in self.stats.items():
            print(f"{stat}: {value}")
