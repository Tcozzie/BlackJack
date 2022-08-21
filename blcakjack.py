import card

# -----------------------

def evaluate(hand):
    result = 0
    aces=0
    for one_card in hand:
        if (one_card.get_value()==11):
            aces+=1
        result += one_card.get_value()

    while result>21 and aces >0:
        result-=10
        aces-=1
        
    return result

# -----------------------

def process_hand(hand):
    #print("The processHand function needs to be completed")
    score=evaluate(hand)
    print("You've got..."+str(score))
    

# -----------------------

def main():

    ace = card.Card("ace", "spades")
    king = card.Card("king", "diamonds")
    queen = card.Card("queen", "hearts")
    jack = card.Card("jack", "clubs")
    ten = card.Card("ten", "spades")
    nine = card.Card("nine", "hearts")
    eight = card.Card("eight", "diamonds")
    seven = card.Card("seven", "clubs")
    six = card.Card("six", "spades")
    five = card.Card("five", "hearts")
    four = card.Card("four", "diamonds")
    three = card.Card("three", "clubs")
    two = card.Card("two", "spades")

    process_hand([ace, king])
    process_hand([queen, ace])
    process_hand([ace, jack])
    process_hand([ten, ace])
    process_hand([two, three, four, five, six, seven])
    process_hand([eight, nine, two])
    process_hand([two,three,four,five,six,ace])
    process_hand([ace,jack,ace])

# -----------------------

main()
