import random

print("--- ACEY DEUCEY ---") # title

instructions = ""

while instructions not in ['y','n'] :
    instructions = input("\nInstructions? (y/n) >>> ")

    if instructions == 'y':
        print("\nAcey Deucey is a simple card game.\nTwo cards are drawn and the player places a bet on whether the next card drawn will fall between the two cards.\n\nYou play against the computer, starting with $50.\nEach round costs an ante of $1, which is doubled every five rounds.\n\nIf you wish to pass, enter a bet of $0.\nHowever, you must still pay the ante.\n\nHave fun!\n\n")

# function and variable definition / initialisation

computer_money = 50
player_money = 50
bank = 10

bet = 100 
ante = 1

leftCard = 0
rightCard = 0
middleCard = 0

max_bet = 0

round = 0


#to make it Tidy it only can use Definition 
#card creation 
def printCards(leftCard, middleCard, rightCard):
    print(' ', '_'*7, ' '*4, '_'*7, ' '*4, '_'*7, sep='', )
    #leftCard first Line 
    print('|', format(leftCard, '<7d'),'|', sep='', end = "")
    #middle card first line 
    print('  ', '|', format(str(middleCard), '7s'),'|', sep='', end = "")
    #right card first line 
    print('  ', '|', format(rightCard, '<7d'), '|', sep='') 

    print('|',' '*7, '|', ' '*2, '|',' '*7, '|', ' '*2, '|',' '*7, '|', sep='') 
    print('|',' '*7, '|', ' '*2, '|',' '*7, '|', ' '*2, '|',' '*7, '|', sep='') 
    print('|',' '*7, '|', ' '*2, '|',' '*7, '|', ' '*2, '|',' '*7, '|', sep='')  
    print('|',' '*7, '|', ' '*2, '|',' '*7, '|', ' '*2, '|',' '*7, '|', sep='') 
    #left last line
    print('|', format(leftCard, '>7d'),'|', sep='', end = "")
    #middle last line
    print('  ', '|', format(str(middleCard), '>7s'),'|', sep='', end = "")
    #right last line
    print('  ', '|', format(rightCard, '>7d'), '|', sep='') 

    print(' ', '_'*7, ' '*4, '_'*7, ' '*4, '_'*7, sep='', )



play_game = input("\nDo you wish to play a round? (y/n) >>> ")

while play_game == "y":
    bet = 100 

    leftCard = random.randint(1, 13)
    rightCard = random.randint(1, 13)

    if leftCard > rightCard:
        temp = leftCard
        leftCard = rightCard
        rightCard = temp

    if leftCard > rightCard:
        

        if leftCard > rightCard:
           leftCard , rightCard = rightCard , leftCard 

        

    middleCard = random.randint(1, 13) # random amount from middle card 

    bank += ante * 2
    player_money -= ante
    computer_money -= ante

    print("\nAnte added to pot.")

    print("\nPlayer: ",player_money," Computer: $",computer_money)
    print("Pot: $", bank, "Ante: ",ante)

    print("\n[PLAYER] Cards are: \n")

    printCards(leftCard, "?", rightCard)

    max_bet = min(player_money, bank)

    while bet > max_bet:
        bet = int(input(f"\nEnter bet (max ${max_bet}) >>> $"))

    if bet == 0:
        print("\n[PLAYER] PASS!")
    else:
        printCards(leftCard, middleCard, rightCard)

        if middleCard == rightCard or middleCard == leftCard: 
            print("\n[PLAYER] HIT THE POST!!!")
            print("[PLAYER] You lose $", bet*2)
            player_money -= 2 * bet
            bank += 2 * bet
        elif middleCard > leftCard and middleCard < rightCard:
            print("\n[PLAYER] You win $", bet)
            player_money += bet
            bank -= bet
        else:
            print("\n[PLAYER] You lose $", bet)
            player_money -= bet
            bank += bet

    print("\nPRESS <ENTER> TO CONTINUE")
    input() 

    leftCard = random.randint(1, 13)
    rightCard = random.randint(1, 13)

    while leftCard == rightCard:
        rightCard = random.randint(1, 13) # make sure numbers are not the same

    if leftCard > rightCard:
        
     middleCard = random.randint(1, 13)

    print('[COMPUTER]  Cards are:\n')

    printCards(leftCard, "?", rightCard)

    max_bet = min(computer_money, bank) # to make sure amount are not over than the pot or the real money you just have 
    
   
    
    
    while bet > max_bet:
        bet = random.randint(0, max_bet)
        print(f"\nEnter bet (max ${max_bet}) => ${bet}")

    if bet == 0:
        print("\n[COMPUTER] PASS!")
    else:
        printCards(leftCard, middleCard, rightCard)

        if middleCard == rightCard or middleCard == leftCard: 
            print("\n[COMPUTER] HIT THE POST!!!")
            print("[COMPUTER] You lose $", bet*2)
            computer_money -= 2 * bet
            bank += 2 * bet
        elif middleCard > leftCard and middleCard < rightCard:
            print("\n[COMPUTER] You win $", bet )
            computer_money += bet
            bank -= bet
        else:
            print(f"\n[COMPUTER] You lose ${bet}")
            computer_money -= bet
            bank += bet

        print("\nPlayer: $",player_money, "Computer: $",computer_money)
    print("Pot: $", bank, "Ante:", ante)

    if player_money <= 0:
        print("player is broke! $" ,player_money)
        play_game = "n"
    if computer_money <= 0:
        print("\nComputer is broke" ,computer_money)
        play_game = "n"

    play_game = input("\nDo you wish to play another round? (y/n) >>> ")
    round += 1

print("\n--- GAME SUMMARY ---\n")
print("Player: $",player_money, "Computer: $",computer_money)
print("Pot: $",bank, "Ante: $",ante, )
print("You played ",round, "rounds")
    
    
