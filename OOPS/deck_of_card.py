"""
In this method we have to Shuffle the cards using Random method and then distribute 9 Cards to 4 Players
and Print the Cards the received by the 4 Players using 2D Array…

Author: Shruti Zarbade
Date: 28/01/2020

"""
import random


class DeckOfCard:
    """This class contains deck of cards having suit and rank which can be
    shuffled and distributed among 4 player
    """
    def __init__(self):
        self.suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = []

    def pack_of_cards(self):
        """This method creates a deck of 52 cards
        :return: self.cards: a list of cards
        """
        for i in self.suit:
            for j in self.rank:
                self.cards.append(j + " : " + i)  # Appending the possible cards in the empty list
        return self.cards

    def card_distribution(self):
        """This method randomly distributed card among the four player
        :return: prints the cards distributed to the four players
        """

        shuffle_cards = random.sample(self.pack_of_cards(), 36)  # 36 is the total cards needed(9*4)

        # dividing 9  cards among player

        cards_of_players = []

        cards_of_players.append(shuffle_cards[:9])
        cards_of_players.append(shuffle_cards[9:18])
        cards_of_players.append(shuffle_cards[18:27])
        cards_of_players.append(shuffle_cards[27:])

        print(f"Distribution of Cards among 4 players: {cards_of_players}")
        print()

        return cards_of_players


if __name__ == '__main__':
    deck = DeckOfCard()
    deck.card_distribution()

