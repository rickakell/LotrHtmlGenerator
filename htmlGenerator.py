import csv
from card import Card

with open("cardList.csv", 'r', encoding="ANSI", errors="ignore") as csvfile:
    cardList = csv.reader(csvfile)
    counter = 0
    for card in cardList:
        if counter == 1:
            tempCard = Card(card)
            tempCard.writeHtmlFile()
        else:
            counter += 1