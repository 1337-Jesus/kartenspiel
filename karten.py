#!/usr/bin/env python3
import random

farben = ['Pik', 'Kreuz', 'Herz', 'Karo']
namen = ['Ass', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'Koenig']

startDeck = []

def createDeck(deck):
    for i in farben:
        for w, n in enumerate(namen):
            deck.append({'farbe': i, 'name': n, 'wert': w})
    return(deck)


def shuf(deck):
    deckout = deck.copy()
    random.shuffle(deckout)
    return(deckout)

playdeck = createDeck(startDeck)

for i in playdeck:
    print(i)

playdeckshuffled = shuf(playdeck)

for i in playdeckshuffled:
    print(i)

