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

def dealerActions():
    dealerTotal = calculate(dealerHand)
    if dealerTotal[0] <= 16:
        dealerHand.append(random.choice(cards))
    if(dealerTotal[0] > 21):
        print("DEALER BUST.")
        exit

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
                calculate(currentHand)
                print("Total: %2d/%2d" % (calculate(currentHand)[0], calculate(currentHand)[1]))
                if(calculate(currentHand)[0]) > 21:
                    print("PLAYER BUST")
                    playerCash -= bet
                    break
                dealerActions()
            case "s":
                print("Stand")
                print("Totals: %2d/%2d" % (calculate(currentHand)[0], calculate(currentHand)[1]))
                dealerActions()
                print("Dealer Totals: %2d/%2d" % (calculate(dealerHand)[0],calculate(dealerHand)[1]))
                if(calculate(dealerHand)[0] > 21):
                    print("Dealer bust. You win.")
                    playerCash += bet
                elif(calculate(currentHand)[1] > 21):
                    if(calculate(dealerHand)[1] <= 21):
                        if(calculate(currentHand)[0] > calculate(dealerHand)[0] and calculate(currentHand)[0] > calculate(dealerHand)[1]):
                            print("You have more than the Dealer. You win.")
                            playerCash += bet
                        elif(calculate(currentHand[0] == calculate(dealerHand[0]))):
                            print("DRAW.")
                        else:
                            print("Dealer has more. You lose.")
                            playerCash -= bet
                else:
                    print("You have more than the dealer. You win.")
                    playerCash += bet
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
            break
        finally:
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
        dealerHand.append(random.choice(cards))
        currentHand.append(random.choice(cards))

    cardsInPlay.append(dealerHand)
    cardsInPlay.append(currentHand)

    print("Cards in Play: ", end = "")
    print(cardsInPlay)
    print()
    print("Here are your cards.")
    for card in currentHand:
        print(card)
    print("Total: %2d/%2d" % (calculate(currentHand)[0], calculate(currentHand)[1]))
    if(calculate(currentHand)[1]) == 21:
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