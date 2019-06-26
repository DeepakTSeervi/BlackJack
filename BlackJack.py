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
            self.balance = self.balance + withdraw_amount  
            return 0

    def __str__(self):
        return f"{self.name} has {self.balance} coins"
		
if __name__ == '__main__':
    print("-----**WELCOME**-----")
    print("lets play Blackjack")

    #taking user inputs 
    name = input("Enter your name : ")
    balance = input("Enter the amount you want to deposit : ")
    
    # list for human player
    player_cards = []
    total = 0
    # list for computer
    computer_cards = []
    
    # creating an object for each player
    player = Bank(name, balance)
    computer = Bank('computer', balance)
    
    # displaying the cards of human player
    print(name + ' has the following cards :')
    
    # getting random cards from random_card()
    player_cards.append(random_card())
    player_cards.append(random_card())

    computer


    while True:
        
        # printing all the cards of players
        for x in player_cards:
            print(player_cards)

            # checking the best condition for picking 1 or 10 in the occurance of ace
            if x == 'ace' and total + cards[x][1] >= 21:
                total = total + cards[x][0]
            elif x == 'ace':
                total = total + cards[x][1]
            else:
                total = total + cards[x]


        if total >= 21:
            print(f"You lose :( \nComputer wins\nYour total goes to {total}")
            break
        else:
            print(f"{total} is your total")
            descision = input("Hit or Stay?(h/s)")
            if descision == 'h':
                player_cards.append(random_card())

            else:
                break

            

