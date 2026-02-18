""""
Alice has some cards with numbers written on them.
She arranges the cards in decreasing order and lays them out face down in a sequence on a table.
She challenges BOB to pick out the containing a given number by turning over as few cards as possible
Write a function to help Bob locate the card as quickly as possible

input : list_of_cards, card_to_pick
output: If card is found then print the card to pick if not found print -1

Edge Cases:

1) List can be empty -1
2) List wont have the card -1

Test-Cases
3) It may be the start of LHS
4) It may be end of LHS
5) It may also happen that element can be repeated again
"""

# BRUTE FORCE SOLUTION
# Linear search
"""
Iterate the list and check if the element is present in that list
"""
def fetch_the_card(list_of_cards,card_to_pick):
    for card in list_of_cards:
        if card == card_to_pick:
            return card
    return -1

if __name__=="__main__":
    list_of_cards=[0,1,3,4,5,311,6724,6,6,7,8,8,9,10]
    print(fetch_the_card(list_of_cards,0))
    print(fetch_the_card(list_of_cards,102))
    print(fetch_te_card(list_of_cards,200))

