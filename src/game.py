from .player import Player

class Game:
    def __init__(self, player1_name, player2_name, rounds=10):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.rounds = rounds
        self.current_round = 1

    def start_game(self):
        print(f"Starting game between {self.player1.name} and {self.player2.name}")
        while self.current_round <= self.rounds:
            print(f"\nRound {self.current_round}")
            self.play_round()
            self.current_round += 1
        self.declare_winner()

    def play_round(self):
        # Each player draws a card
        card1 = self.player1.draw_card()
        card2 = self.player2.draw_card()

        print(f"{self.player1.name} drew: {card1}")
        print(f"{self.player2.name} drew: {card2}")

        # Simulate some basic gameplay mechanics (customize this as needed)
        if card1 and card2:
            # Example: You can implement custom logic for resolving a round here
            winner = self.resolve_round(card1, card2)
            if winner == 1:
                print(f"{self.player1.name} wins this round!")
                self.player1.add_points(1)
            elif winner == 2:
                print(f"{self.player2.name} wins this round!")
                self.player2.add_points(1)
            else:
                print("This round is a tie!")

    def resolve_round(self, card1, card2):
        # Basic resolution logic (you can modify this based on your card mechanics)
        # For example, you could compare specific card abilities or names here.
        if card1.name == "Vini" and card2.name == "Vici":
            return 1  # Example: Player 1 wins if they play "Vini" vs "Vici"
        elif card1.name == "Vici" and card2.name == "Vini":
            return 2  # Example: Player 2 wins if they play "Vici" vs "Vini"
        else:
            return 0  # Tie for simplicity

    def declare_winner(self):
        if self.player1.points > self.player2.points:
            print(f"\n{self.player1.name} wins the game with {self.player1.points} points!")
        elif self.player2.points > self.player1.points:
            print(f"\n{self.player2.name} wins the game with {self.player2.points} points!")
        else:
            print("\nThe game is a tie!")

if __name__ == "__main__":
    # Example of starting a game
    game = Game("Alice", "Bob")
    game.start_game()
