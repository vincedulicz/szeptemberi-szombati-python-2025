import random
from abc import ABC, abstractmethod

SUITS = ['♥', '♦', '♣', '♠']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        if self.rank == 'A':
            return 11
        return int(self.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_score(self):
        score = 0
        ace_count = 0
        for card in self.cards:
            score += card.get_value()
            if card.rank == 'A':
                ace_count += 1

        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
        return score

    def clear(self):
        self.cards = []

    def __str__(self):
        return " ".join(str(c) for c in self.cards)


class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def receive_card(self, card):
        self.hand.add_card(card)

    def get_score(self):
        return self.hand.calculate_score()

    def reset(self):
        self.hand.clear()

    @abstractmethod
    def make_move(self, game):
        pass


class HumanPlayer(Player):
    def make_move(self, game):
        pass


class Dealer(Player):
    def make_move(self, game):
        while self.get_score() < 17:
            card = game.deck.deal()
            if card:
                self.receive_card(card)
                print(f"Osztó húzott: {card}")


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = HumanPlayer("Játékos")
        self.dealer = Dealer("Osztó")

    def play(self):
        print("--- Blackjack OOP Python ---")
        self.deck.reset()
        self.player.reset()
        self.dealer.reset()

        for _ in range(2):
            self.player.receive_card(self.deck.deal())
            self.dealer.receive_card(self.deck.deal())

        self.print_status(reveal_dealer=False)

        if self.player.get_score() == 21:
            print("Blackjack! Nyertél!")
            return

        while True:
            choice = input("Kérsz lapot? (h - hit / s - stand): ").lower()
            if choice == 'h':
                card = self.deck.deal()
                self.player.receive_card(card)
                print(f"Húztál: {card}")
                self.print_status(reveal_dealer=False)
                if self.player.get_score() > 21:
                    print("Besokalltál! Vesztettél.")
                    return
            elif choice == 's':
                break

        print("\nOsztó köre...")
        self.dealer.make_move(self)

        self.print_status(reveal_dealer=True)
        self.determine_winner()

    def print_status(self, reveal_dealer):
        print(f"\n{self.player.name} lapjai: {self.player.hand} (Pont: {self.player.get_score()})")
        if reveal_dealer:
            print(f"{self.dealer.name} lapjai: {self.dealer.hand} (Pont: {self.dealer.get_score()})")
        else:
            first_card = self.dealer.hand.cards[0] if self.dealer.hand.cards else "?"
            print(f"{self.dealer.name} lapjai: {first_card} [Rejtett]")

    def determine_winner(self):
        p_score = self.player.get_score()
        d_score = self.dealer.get_score()

        if d_score > 21:
            print("Az osztó besokallt! Nyertél!")
        elif p_score > d_score:
            print("Nyertél! Magasabb pontszám.")
        elif p_score < d_score:
            print("Vesztettél. Az osztónak több pontja van.")
        else:
            print("Döntetlen (Push).")


if __name__ == "__main__":
    game = BlackjackGame()
    while True:
        game.play()
        if input("\nÚj játék? (i/n): ").lower() != 'i':
            break











