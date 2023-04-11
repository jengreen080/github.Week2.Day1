class Team: 
    points = 0
    def __init__(self, team_name, list_of_players, coach_name):
        self.name = team_name    
        self.players = list_of_players
        self.coach = coach_name

    def add_player(self, new_player):
        return self.players.append(new_player)
    
    def has_player(self, new_player):
        for player in self.players:
            if player == new_player:
                return True
        else:
                return False
        
    def play_game(self, result):
        if result == True:
            points = points + 3
        else: 
            points += 0
        # return points
            
        
