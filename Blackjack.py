import random

# Blackjack Cards

def calculate(hand):
    totals = [0, 0]
    for card in hand:
        if(card.isalpha() and card != "A"):
            value = 10
            totals[0] += value
            totals[1] += value
            continue
        elif(card == "A"):
            value = 1
            value1 = 11
            totals[0] += value
            totals[1] += value1
            continue
        else:
            value = int(card)
            totals[0] += value
            totals[1] += value
    return totals

def selectChoice(playerCash, bet):
    endFlag = False
    while(not endFlag):
        choice = ""
        while choice not in choices:
            choice = input("Select Action: H, S\n").lower()
        match choice:
            case "h":
                print("Hit")
                currentHand.append(random.choice(cards))
                changedHand = calculate(currentHand)
                print("Total: {}/{}".format(changedHand[0], changedHand[1]))
                if(changedHand[0] > 21):
                    print("PLAYER BUST")
                    playerCash -= bet
                    break
                calculatedDealerHand = calculate(dealerHand)
                if(calculatedDealerHand[0] <= 16):
                    dealerHand.append(random.choice(cards))
                    calculatedDealerHand = calculate(dealerHand)
                if(calculatedDealerHand[0] > 21):
                    print("DEALER BUST.")
                    playerCash += bet
                    endFlag = True
            case "s":
                calculatedCurrentHand = calculate(currentHand)
                print("Stand")
                print("Total: {}/{}".format(calculatedCurrentHand[0], calculatedCurrentHand[1]))
                calculatedDealerHand = calculate(dealerHand)
                
                
                while(calculatedDealerHand[0] <= 16):
                    dealerHand.append(random.choice(cards))
                    calculatedDealerHand = calculate(dealerHand)
                
                if(calculatedDealerHand[0] > 21):
                    print("DEALER BUST.")
                    playerCash += bet
                    endFlag = True
                print("Dealer Total: {}/{}".format(calculatedDealerHand[0],calculatedDealerHand[1]))
                
                if(calculatedDealerHand[0] > 21):
                    print("Dealer bust. You win.")
                    playerCash += bet
                    endFlag = True
                
                elif(calculatedCurrentHand[1] <= 21):
                    if((calculatedCurrentHand[0] > calculatedDealerHand[0] and calculatedCurrentHand[0] > calculatedDealerHand[1])
                       or (calculatedCurrentHand[1] > calculatedDealerHand[0] and calculatedCurrentHand[1] > calculatedDealerHand[1])):
                        print("You have more than the dealer.")
                        playerCash += bet
                        endFlag = True
                    elif(calculatedCurrentHand[0] == calculatedDealerHand[0] or calculatedCurrentHand[1] == calculatedDealerHand[1]):
                        print("DRAW")
                        endFlag = True
                    else:
                        print("Dealer has more. You lost.")
                        playerCash -= bet
                        endFlag = True
                else:
                    print("Dealer has more. You lost.")
                    playerCash -= bet
                    endFlag = True
                endFlag = True
    return playerCash
    
print("\nWelcome to Blackjack!\n")

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

while True:
    
    try:
        playerCash = int(input("Input Your Starting Pool of Cash: "))
    except ValueError:
        print("Not a valid number, please try again. ")
    else:
        break

def bet():
    while True:
        try:
            bet = int(input("How much will you bet?: "))
        except ValueError:
            print("Not a valid number, please try again.")
        else:
            return bet

while(playerCash > 0):
    print("Player Pool: %2d" % playerCash)

    currentHand = []
    dealerHand = []
    cardsInPlay = []

    currentBet = bet()

    while(currentBet > playerCash):
        print("Current Bet is higher than remaining Player Cash Pool.")
        currentBet = bet()

    print("Let's deal.")
    while len(dealerHand) < 2:
        # dealerHand.append("9")
        # currentHand.append("9")
        dealerHand.append(random.choice(cards))
        currentHand.append(random.choice(cards))

    cardsInPlay.append(dealerHand)
    cardsInPlay.append(currentHand)

    calculatedCurrentHand = calculate(currentHand)
    calculatedDealerHand = calculate(dealerHand)

    print("Cards in Play: ", end = "")
    print(cardsInPlay)
    print()
    print("Here are your cards.")
    for card in currentHand:
        print(card)
    print("Total: {}/{}".format(calculatedCurrentHand[0], calculatedCurrentHand[1]))
    if(calculatedCurrentHand[1]) == 21:
        print("JACKPOT")
        playerCash += (currentBet * 1.5)
        continue
    print("Dealer's Hand:")
    print(dealerHand[0] + "\n?")

    print("\nHit(H)")
    print("Stand(S)")

    choices = ["h","s"]

    playerCash = selectChoice(playerCash, currentBet)
else:
    print("Cash Pool Depleted. You lose!")