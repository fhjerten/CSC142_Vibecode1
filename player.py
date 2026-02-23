class Player:
    def __init__(self, team, gender, number, name, stats):
        self.team = team
        self.gender = gender  #M or F
        self.number = int(number)  #players number
        self.name = name.strip()
        self.stats = stats

    def __str__(self):
        return f"{self.number} - {self.name}"


        # function for printing all the stats for selected player
    def display_stats(self):
        print(f"\nStats for {self.name} (#{self.number})")
        for stat, value in self.stats.items():
            print(f"{stat}: {value}")


    # Used for helping search a player by name, 
    # for example searchin "joh" will be a match with "john"
    def name_matches(self, search_name):
        return search_name.lower() in self.name.lower()
