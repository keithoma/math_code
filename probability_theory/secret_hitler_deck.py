#!/usr/bin/python

"""
12th of July 2020

Very work in progress.
"""

import random

class SecretHitler():
    def __init__(self):
        self.create_deck()
        self.counter = 0
        self.cards = [None, None, None]

    def create_deck(self):
        self.deck = ['L' if _ <= 5 else 'F' for _ in range(17)]
        random.shuffle(self.deck)
    
    def draw_three(self):
        for i in range(3):
            self.cards[i] = self.deck[self.counter]
            self.counter += 1
        return self.cards

    def remove_card(self, index):
        self.cards[index] = None
        return self.cards

def game():
    game_object = SecretHitler()
    while True:
        print(game_object.draw_three())
        index = int(input("Enter the number of the card you want to remove."))
        print(game_object.remove_card(index))
        index = int(input("Enter the number of the card you want to remove."))
        print(game_object.remove_card(index))


def main():
    game()

if __name__ == "__main__":
    main()