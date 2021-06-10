class Player:
    def __init__(self, name):
        self.health = 1
        self.bullets = 0
        self.is_defending = False
        self.name = name

    def reload(self):
        self.bullets += 1

    def shoot(self, opponent):
        if self.bullets >= 1:
            self.bullets -= 1
            if not opponent.is_defending:
                opponent.health -= 1
        else:
            print(self.name, " has no bullets")

    def defend(self):
        self.is_defending = True


player1 = Player("Player 1")
player2 = Player("Player 2")
end_game = False

while player1.health >= 1 and player2.health >= 1 and not end_game:
    print("Player 1 has", player1.health, "health and", player1.bullets, "bullets")
    print("Player 2 has", player2.health, "health and", player2.bullets, "bullets")

    player1_action = input("Should Player 1 shoot, defend, or reload? (type 'end game' to quit): ")

    if player1_action == "defend":
        player1.defend()
    if player1_action == "reload":
        player1.reload()

    player2_action = input("Should Player 2 shoot, defend, or reload? (type 'end game' to quit): ")

    if player2_action == "defend":
        player2.defend()
    if player2_action == "reload":
        player2.reload()

    if player1_action == "shoot" and player2_action == "shoot":
        player1.bullets -= 1
        player2.bullets -= 1
    else:
        if player1_action == "shoot":
            player1.shoot(player2)
        if player2_action == "shoot":
            player2.shoot(player2)

    player1.is_defending = False
    player2.is_defending = False
    if player1_action == "end game" or player2_action == "end game":
        end_game = True

if player1.health == 0:
    print("Player 2 has won")
elif player2.health == 0:
    print("Player 1 has won")
elif end_game:
    print("This game was stopped early. No winner was decided.")