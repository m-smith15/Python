players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    new_team = []

    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]
        Player.new_team.append(self)
    
    def display_player(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)
        return print("----")

    @classmethod
    def get_team(cls,team_list):
        for players in cls.new_team:
            print(players.team)
        return cls


example1 = Player(players[0])
example2 = Player(players[1])
example3 = Player(players[2])
print(example1.display_player())
print(example2.display_player())
print(example3.display_player())
Player.get_team(players)