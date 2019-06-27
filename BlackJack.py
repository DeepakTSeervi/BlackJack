import random

# creating a dictionary represting all cards along with their values 
cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': (1, 10)}

def random_card():
    '''
    returns a random card
    NOTE: This returns key of the dictionary not the value for the key
    '''
    return random.choice(list(cards.keys()))

class Bank():
    """Having the information about the balance
       for player and computer"""
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount

    
    def withdraw(self, withdraw_amount):
        if self.balance < withdraw_amount:
            return -1
        else:
            self.balance = self.balance - withdraw_amount  
            return self.balance

    def __str__(self):
        return f"{self.name} has {self.balance} coins"
        
if __name__ == '__main__':
    print("-----**WELCOME**-----")
    print("lets play Blackjack")

    #taking user inputs 
    name = input("Enter your name : ")
    balance = input("Enter the amount you want to deposit : ")
    
    # list of cards for human player
    player_cards = []
    player_total, computer_total = 0, 0
    turn = 0
    # list of cards for computer
    computer_cards = []
    
    # creating an object for each player
    player = Bank(name, balance)
    computer = Bank('computer', balance)
    
    # displaying the cards of human player
    print(name + ' has the following cards :')

    # getting two random cards from random_card() for player
    player_cards.append(random_card())
    player_cards.append(random_card())

    # getting two random cards from random_card() for computer
    computer_cards.append(random_card())
    computer_cards.append(random_card())


    betting_amount = input('Enter the amount you want to bet : ')
    while True:
        """
        This section is for Player
        """
        if turn%2 == 0:
            # printing all the cards of players
            for x in player_cards:
                print(player_cards)

                # checking the best condition for picking 1 or 10 in the occurance of ace
                if x == 'ace' and player_total + cards[x][1] >= 21:
                    player_total = player_total + cards[x][0]
                elif x == 'ace':
                    player_total = player_total + cards[x][1]
                else:
                    player_total = player_total + cards[x]


            """
            BlackJack yet to complete------------
            """
            if player_total >= 21:
                print(f"{name} loses :) \nComputer wins\n{name} total goes to {player_total}\nComputer total goes to {computer_total}")
                player.withdraw(betting_amount)
                computer.deposit(betting_amount)
                print(player, '\n', computer)
                
                replay = input('Do you want to continue the game?(y/n)  ')
                if replay == 'y':
                    break
                else:
                    exit()

            else:
                print(f"{player_total} is your total")
                descision = input("Hit or Stay?(h/s)")

                # if player hits
                if descision == 'h':
                    player_cards.append(random_card())
                else:
                    turn += 1

        """
        This section is for Computer
        """
        if turn%2 != 0:
            print('Computer has the following cards :')
            # printing all the cards of players
            for x in computer_cards:
                print(computer_cards)

                # checking the best condition for picking 1 or 10 in the occurance of ace
                if x == 'ace' and computer_total + cards[x][1] >= 21:
                    computer_total = computer_total + cards[x][0]
                elif x == 'ace':
                    computer_total = computer_total + cards[x][1]
                else:
                    computer_total = computer_total + cards[x]

            """
            BlackJack yet to complete------------
            """
            if computer_total > 21:
                print(f"Computer loses :( \n{name} wins\n{name} total goes to {player_total}\nComputer total goes to {computer_total}")
                player.deposit(betting_amount)
                computer.withdraw(betting_amount)
                print(player, '\n', computer)
                
            else:
                print(f"{computer_total} is computer's total")


                if player_total > computer_total:
                # if computer hits 
                    player_cards.append(random_card())
                else:
                    turn += 1
                

                

            

