# Import library
from random import randint  # Random integer library


class BlackjackGame:
    # Variables
    def __init__(self):
        # Score variables
        self.game_played = 0
        self.player_wins = 0
        self.dealer_wins = 0
        self.ties = 0

        # Hand value variable
        self.user_hand = 0
        self.dealer_hand = 0

        # User input and game variable
        self.game_over = False
        self.stop_game = False
        self.user_input_value = 1

    # Show game menu
    @staticmethod
    def show_game_menu():
        print('1. Get another card')
        print('2. Hold hand')
        print('3. Print statistics')
        print('4. Exit \n')

    # Find the cards value
    @staticmethod
    def card_value(value):
        card_value = {1: 'ACE!', 11: 'JACK!', 12: 'QUEEN!', 13: 'KING!'}
        if value == 1 or value >= 11:
            return card_value[value]
        else:
            return value

    # User input
    def user_input(self):
        flag = True  # Flag to check if the user input is between a range
        user_inp = int(input('Choose an option: '))  # User input variable

        # While flag is true keep repeating
        while flag:
            # Check if user input is between 1 and 4
            if 1 <= user_inp <= 4:
                self.user_input_value = user_inp
                flag = False
            else:
                # If user input is not between 1 and 4 keep asking
                # Show ERROR message
                print('\nInvalid input!')
                print('Please enter an integer value between 1 and 4. \n')

                # Show game menu again
                self.show_game_menu()

                # Ask for the value again
                user_inp = int(input('Choose an option: '))
                self.user_input_value = user_inp

    # User hand
    def user_dealt(self):
        # Generate a random number
        random_number = randint(1, 13)

        # Find the card value
        card_values = self.card_value(random_number)  # Card values ~ (ACE, JACK, QUEEN, KING)
        print(f'\nYour card is a {card_values}!')  # Show card dealt

        # Check if the card is a (ACE, JACK, QUEEN, KING)
        if random_number >= 11:
            # If the card is (ACE, JACK, QUEEN, KING) add 10 to the variable
            self.user_hand += 10  # Add the value to the variable
        else:
            # Add the random number to the variable
            self.user_hand += random_number  # Add the value to the variable

        print(f'Your hand is: {self.user_hand} \n')

        # Check if user hand is over or equal to 21
        if self.user_hand > 21:
            self.dealer_wins += 1
            print('Dealer wins!\n')
            self.game_over = True
        elif self.user_hand == 21:
            self.player_wins += 1
            print('Player wins!\n')
            self.game_over = True

    # Dealer hand
    def dealer_dealt(self):
        # Generate random number
        self.dealer_hand = randint(16, 26)

        print(f"\nDealer's hand: {self.dealer_hand}")
        print(f'Your hand is: {self.user_hand}\n')

        # Check who wins the game
        if self.dealer_hand > 21:
            self.player_wins += 1
            print('You win!\n')
            self.game_over = True
        elif self.dealer_hand == 21:
            self.dealer_wins += 1
            print('Dealer wins!\n')
            self.game_over = True
        elif self.dealer_hand == self.user_hand:
            self.ties += 1
            print("It's a tie! No one wins!\n")
            self.game_over = True
        elif self.user_hand > self.dealer_hand:
            self.player_wins += 1
            print('You win!\n')
            self.game_over = True
        elif self.dealer_hand > self.user_hand:
            self.dealer_wins += 1
            print('Dealer wins!\n')
            self.game_over = True

    # Show game statistics
    def game_statistics(self):
        print(f'\nNumber of Player wins: {self.player_wins}')
        print(f'Number of Dealer wins: {self.dealer_wins}')
        print(f'Number of tie games: {self.ties}')
        print(f'Total # of games played is: {self.game_played}')
        if self.player_wins == 0 and self.game_played == 0:
            print('Percentage of Player wins: 0%\n')
        else:
            print(f'Percentage of Player wins: {round((self.player_wins / self.game_played) * 100)}%\n')

    # Game logic
    def game_logic(self):
        print(f'START GAME #{self.game_played+1}')
        while not self.game_over:
            if self.user_input_value == 1:
                self.user_dealt()  # Dealt a car for the user
                if not self.game_over:
                    self.show_game_menu()  # Show game menu
                    self.user_input()  # Ask for user input
            elif self.user_input_value == 2:
                self.dealer_dealt()  # Dealt a car for the dealer
                self.user_input_value = 1  # Reset user input value
            elif self.user_input_value == 3:
                self.game_statistics()  # Show game statistics
                self.show_game_menu()  # Show game menu
                self.user_input()  # Ask for user input
            else:
                self.game_over = True
                self.stop_game = True


if __name__ == '__main__':
    # Game object
    game = BlackjackGame()

    while not game.stop_game:
        game.game_logic()  # Play the game
        game.game_played += 1  # Count the games played
        game.user_hand, game.dealer_hand = 0, 0  # Reset hand to 0
        game.game_over = False  # Reset the game
