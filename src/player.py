from src.deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
        self.hand = []
        self.discard_pile = []
        self.points = 0
        self.message_queue = []

    def draw_card(self):
        card = self.deck.draw_card()
        if card:
            self.hand.append(card)
        else:
            print("No cards to draw!")
        return card

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            self.discard_pile.append(card)
            return card
        print(f"{card.title} is not in your hand.") # this shouldn't be possible but is included for safety
        return None

    def discard_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            self.discard_pile.append(card)
        else:
            print(f"{card.title} is not in your hand to discard.") # this shouldn't be possible but is included for safety

    def show_hand(self):
        for card in self.hand:
            print(f"{card.title}: {card.description}")

    def show_discard_pile(self):
        for card in self.discard_pile:
            print(f"{card.title}: {card.description}")

    def add_points(self, points):
        self.points += points

    def reset_deck(self):
        self.deck.cards = self.discard_pile
        self.discard_pile = []
        self.deck.shuffle()

    def add_message(self, message):
        self.msg_queue.append(message)

    def display_message_queue(self):
        for message in self.message_queue:
            print(message)

    def clear_message_queue(self):
        self.message_queue.empty()

    def __str__(self):
        return f"{self.name} (Current score: {self.points})"

