from enum import Enum
from src.game.event import EventObserver, Events


class Players(Enum):
    PLAYER = 'player'
    OPPONENT = 'opponent'

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return self.value


class Player:
    health = 20
    image = None
    stack = []
    graveyard = []
    hand = []
    table = []
    player_type = None

    def __init__(self, player_type, image: str = None):
        self.image = image
        self.player_type = player_type

    def __str__(self):
        return self.player_type

    def __repr__(self):
        return self.player_type

    def __eq__(self, other):
        return self.player_type == other.player_type

    def __ne__(self, other):
        return self.player_type != other.player_type

    def __str__(self):
        return self.player_type

    def __repr__(self):
        return self.player_type

    def is_opponent(self):
        return self.player_type == Players.OPPONENT

    def revive_card(self, card, to_table=False):
        if card in self.graveyard:
            self.graveyard.remove(card)
            if to_table:
                self.table.append(card)
            else:
                self.hand.append(card)

    def draw_card(self):
        if len(self.hand) > 7:
            self.show_hand()
            card = self.await_choose_card("Choose a card to discard")
            print("Discarding card: ", card)
            self.hand.remove(card)
            self.graveyard.append(card)

        card = self.stack.pop()
        print("Drawing card: ", card)
        self.hand.append(card)

    def destroy_card(self, card):
        print("Destroying card: ", card)
        self.graveyard.append(card)
        if card in self.hand:
            self.hand.remove(card)
        elif card in self.table:
            self.table.remove(card)

    def show_hand(self):
        print("Showing hand:", self.hand)

    def await_choose_card(self):
        print("Chose card 0")
        return self.hand.pop()
