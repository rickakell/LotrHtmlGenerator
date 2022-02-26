import csv
from card import Card

with open("cardList.csv", 'r', encoding="ANSI", errors="ignore") as csvfile:
    cardList = csv.reader(csvfile)
    counter = 0
    for card in cardList:
        if counter < 2 and counter > 0:
            tempCard = Card(card)
            tempCard.writeHtmlFile()
        counter += 1