import random
import time
from constants import *


class Casino():

    def __init__(self):
        self.cash = 100


    def start(self):

        """Function for start menu of project"""

        print('Welcome to the casino!\nSelect the game you want to play:\n1. One-armed Bandit\n2. Roulette\n3. Blackjack\nYour balance is 100$\n')

        while True:
            choice_player = input()
            if choice_player.isdigit():
                break
            if 4 < choice_player < 1:
                print('Enter the name of the game more correctly')

        match choice_player:

            case '1':
                print('Welcome to the One-Armed Bandit game!\nThe rules are simple - you spin the reel, and with three identical numbers you win your bet doubled by two, with three sevens - your bet multiplied by seven')
                self.bandit()

            case '2':
                print('The rules are simple, you bet on the playing field, and if the ball hits your field, you get a win!'
                      '\nIf you bet on 0, you win your bet multiplied by 77\if you bet on a number, you get your bet multiplied by 7'
                      '\nIf you bet on black or red, you will get your bet multiplied by 2')
                self.roulette()

            case '3':
                print('Welcome to Blackjack!\nThe rules are simple, you get the cards until you have 21 points or'
                      'more points than the opponent\nIf you win, you will get your bet multiplied by 2')
                self.black()

    def bandit(self):
        """Function for game bandit"""

        print('If you want to exit the game, enter exit, or pass to continue')
        choice_player = input().lower()
        if choice_player == 'exit':
            self.start()

        if self.cash == 0:
            print("You've run out of money")
            self.bankrot()

        print('Input your bet')
        bet = int(input())
        if bet > self.cash:
            print("You don't have enough money\nEnter your bet again")
            bet = int(input())
        if bet <= 0:
            print('A negative or zero bid is not possible\nEnter your bet again')
            bet = int(input())
        if bet <= self.cash:
            print('The drum is spinning!')
            number_1 = random.randint(1,10)
            number_2 = random.randint(1,10)
            number_3 = random.randint(1,10)
            print(number_1)
            time.sleep(3)
            print(number_2)
            time.sleep(3)
            print(number_3)

            if number_1 == number_2 == number_3:
                print('You have won!')
                self.cash += (bet*2)
                print(f'Your balance = {self.cash} $')

            if number_1 == '7' and number_2 == '7' and number_3 == '7':
                print('YOU HIT THE JACKPOT!!!')
                self.cash += (bet*7)
                print(f'Your balance = {self.cash} $')

            else:
                self.cash -= bet
                print(f"You've lost!\nYour balance = {self.cash} $")
                if self.cash != 0:
                    self.bandit()
                else:
                    self.bankrot()

    def roulette(self):

            """Function for game roulette"""

            print('If you want to exit the game, enter exit, or pass to continue')
            choice_player = input().lower()
            if choice_player == 'exit':
                self.start()

            if self.cash == 0:
                print("You've run out of money")
                self.bankrot()

            print('Enter your bet')
            bet = int(input())
            if bet > self.cash:
                print("You don't have enough money\nEnter your bet again")
                bet = int(input())
            if bet <= 0:
                print('Negative or zero bid is not possible\nEnter your bet again')
                bet = int(input())
            if bet <= self.cash:
                print('Enter zero if you want to put on zero, number to put a digit, or color to put on a color')
                choice = input()
                choice.lower()
                match choice:

                    case 'zero':
                        number = random.randint(0,36)
                        print('The ball is spinning...')
                        time.sleep(3)
                        print(number)
                        if number != 0:
                            self.cash -= bet
                        print(f"You've lost!\nYour balance - {self.cash}")
                        if number == 0:
                            self.cash += (bet*77)
                            print(f'You have won!!!\nYour balance - {self.cash}')
                        if self.cash != 0:
                            self.roulette()
                        else:
                            self.bankrot()


                    case 'number':
                        print('Enter a number from 1 to 36')
                        numbers = int(input())
                        if 1 > numbers or numbers > 37:
                            print('Enter the bet again') #сделать отдельную функцию для каждой ставки в рулетке
                        random_number = random.randint(1,37)
                        print('The ball is spinning...')
                        time.sleep(3)
                        print(random_number)
                        if numbers == random_number:
                            self.cash += (bet*7)
                            print(f'You have won!!!!\nYour balance - {self.cash}')
                        else:
                            self.cash -= bet
                            print(f"You've lost, Your balance - {self.cash}")
                        if self.cash != 0:
                            self.roulette()
                        else:
                            self.bankrot()

                    case 'color':
                        print('Enter red to put on red, or black to put on black')
                        color_choice = input()
                        color_choice.lower()
                        dict = {1:'red', 2:'black'}
                        random_color = random.randint(1,2)
                        print('The ball is spinning...')
                        time.sleep(3)
                        print(f'Color dropped out - {dict[random_color]}')
                        if color_choice == dict[random_color]:
                            self.cash += (bet*2)
                            print(f'You have won! Your balance - {self.cash}')
                        else:
                            self.cash -= bet
                            print(f"You've lost, Your balance - {self.cash}")
                        if self.cash != 0:
                            self.roulette()
                        else:
                            self.bankrot()


    def black(self):
        """Function for game blackjack"""

        def card():
            """Function to take a cards to user"""
            global player_points

            player_1 = random.randint(0, len(stack) - 1)
            player_2 = random.randint(0, len(stack) - 1)
            player_card_1 = stack[player_1]
            player_card_2 = stack[player_2]
            if player_card_1 in stack_numbers:
                player_points += int(stack[player_1])
            if player_card_1 in stack_literas:
                player_points += 10
            if player_card_1 in stack_tuz:
                player_points += 11
            if player_card_2 in stack_numbers:
                player_points += int(stack[player_2])
            if player_card_2 in stack_literas:
                player_points += 10
            if player_card_2 in stack_tuz:
                player_points += 11
            stack.remove(player_card_1)
            stack.remove(player_card_2)
            print(f'Players card - {player_card_1} + {player_card_2} = {player_points}')

        def comp_card():
            """Function to take a cards to computer"""
            global comp_points

            comp_1 = random.randint(0, len(stack) - 1)
            comp_2 = random.randint(0, len(stack) - 1)
            comp_card_1 = stack[comp_1]
            comp_card_2 = stack[comp_2]
            if comp_card_1 in stack_numbers:
                comp_points += int(stack[comp_1])
            if comp_card_1 in stack_literas:
                comp_points += 10
            if comp_card_1 in stack_tuz:
                comp_points += 11
            if comp_card_2 in stack_numbers:
                comp_points += int(stack[comp_2])
            if comp_card_2 in stack_literas:
                comp_points += 10
            if comp_card_2 in stack_tuz:
                comp_points += 11
            stack.remove(comp_card_1)
            stack.remove(comp_card_2)

        def player_extra_card():
            """Function to take extra cards to user"""
            global player_points

            player_extra_card = random.randint(0, len(stack) - 1)
            print(f'You took the card - {stack[player_extra_card]}')
            if stack[player_extra_card] in stack_numbers:
                player_points += int(stack[player_extra_card])
            if stack[player_extra_card] in stack_literas:
                player_points += 10
            if stack[player_extra_card] in stack_tuz:
                player_points += 11
            stack.remove(stack[player_extra_card])
            print(f'You have - {player_points} points')
            if player_points > 21:
                print(f'You lost, your balance - {self.cash}')
                time.sleep(1.5)
                self.black()

        def comp_extra_card():
            """Function to take extra cards to computer"""
            global comp_points
            comp_extra_card = random.randint(0, len(stack) - 1)
            print(f'Your opponent has taken a card')
            if stack[comp_extra_card] in stack_numbers:
                comp_points += int(stack[comp_extra_card])
            if stack[comp_extra_card] in stack_literas:
                comp_points += 10
            if stack[comp_extra_card] in stack_tuz:
                comp_points += 11
            stack.remove(stack[comp_extra_card])
            if comp_points == 21:
                print(f'You lost, your balance - {self.cash}')
                time.sleep(1.5)
                self.black()

        def bankrot():
            print("HA-HA -HA\nYou are a bankrupt and a beggar!\nGet out of my casino")
            time.sleep(3)
            print('You were thrown out of the casino window')
            exit()

        global risk
        global player_points
        global comp_points
        player_points = 0
        comp_points = 0

        if self.cash == 0:
            bankrot()

        print('If you want to exit the game, enter exit, or pass to continue')
        choice = input()
        choice.lower()
        if choice == 'exit':
            self.start()

        print('The values of the cards - from two to ten - from 2 to 10 points, respectively, the ace — 11, king, queen and jack - 10 points\nEnter your bet')
        bet = int(input())
        if bet > self.cash:
            print("You don't have enough money\nEnter your bet again")
            bet = int(input())
        if bet <= 0:
            print('Negative or zero bid is not possible\nEnter your bet again')
            bet = int(input())
        if bet <= self.cash:
            self.cash -= bet
            card()
            comp_card()
            if player_points == 21:
                self.cash += (bet*2)
                print(f'You won, your balance - {self.cash}')
                self.black()
            if comp_points == 21:
                print(f'You lost, your balance - {self.cash}')
                self.black()


            counter = 0

            while player_points < 21:
                print('Do you want to take another card?\nEnter yes to take the card, or no to continue')
                answer = input()
                answer.lower()
                if answer == 'no':
                    print(f'You have - {player_points} points')
                    break
                else:
                    counter += 1
                    player_extra_card()

                if player_points == 21:
                    self.cash += (bet * 2)
                    print(f'You won, your balance - {self.cash}')
                    time.sleep(1.5)
                    self.black()

            risk_1 = 1
            while comp_points < 21:
                print('Your opponent decides whether to take a card\n')
                time.sleep(1.5)
                if counter >= 3:
                    risk *= 0.95
                if counter>=4:
                    risk *= 0.9
                if counter>=5:
                    risk *= 0.85
                if comp_points < 21:
                    if comp_points <= 10:
                        comp_extra_card()

                        if comp_points > 21:
                            self.cash += (bet * 2)
                            print(f'The computer lost, and you won!\nYour balance  - {self.cash}')
                            time.sleep(1.5)
                            self.black()

                    elif comp_points <= 15:
                        risk = random.randint(1,10) * risk_1
                        if risk <= 8:
                            comp_extra_card()
                            if comp_points > 21:
                                self.cash += (bet * 2)
                                print(f'Your opponent lost, and you won, your balance - {self.cash}')
                                time.sleep(1.5)
                                self.black()


                        else:
                            print(f'Your opponent has {comp_points} points' )
                            break
                    elif comp_points <= 17:
                        risk = random.randint(1,10) * risk_1
                        if risk <= 2:
                            comp_extra_card()
                            if comp_points > 21:
                                self.cash += (bet*2)
                                print(f"You've won! - Your balance {self.cash}")
                                self.black()

                        else:
                            print(f'Your opponent has - {comp_points} points')
                            break
                    else:
                        risk = random.randint(1,100) * risk_1
                        comp_extra_card()
                        if comp_points > 21:
                            self.cash += (bet*2)
                            print(f"You've won! - Your balance {self.cash}")
                            self.black()
                        else:
                            print(f'Your opponent has {comp_points}points\n')
                            break
            if player_points == comp_points:
                self.cash += bet
                print(f"Draw, your balance - {self.cash}")
                self.black()

            elif player_points > comp_points:
                self.cash += (bet*2)
                print(f"You've won! - Your balance {self.cash}")
                self.black()

            elif player_points < comp_points and comp_points < 22:
                print(f'You have lost - your balance{self.cash}')
                self.black()
            else:
                self.cash += (bet*2)
                print(f"You've won! - Your balance {self.cash}")
                self.black()




