def main():
    
    game = True
    o = True
    x = False
    o_games = 0
    x_games = 0
    number_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
    print("This is a first to 3 wins match.")
    print()

# calling functions and using them to add letters to certain sections
    while game == True:
        print(f"Scores: o [{o_games} : {x_games}] x")
        print()
        print(*number_list, sep= "/")
        if o == True:
            user = str(input("\no's turn. Choose 1-9: "))
            player_o(user, number_list)
            o_games = outcome_o(number_list, o_games)
            x = True
            o = False
        elif x == True:
            user = str(input("\nx's turn. Choose 1-9: "))
            player_x(user, number_list)
            x_games = outcome_x(number_list, x_games)
            o = True
            x = False



def player_o(user, number_list):
    if user == "6":
        user = "6\n"
    elif user == "3":
        user = "3\n"
    for i in range (len(number_list)):
        if user == number_list[i]:
            if i == 6 or i == 3:
                number_list[i] = "o\n"
            else:
                number_list[i] = "o"


def player_x(user, number_list):
    if user == "6":
        user = "6\n"
    elif user == "3":
        user = "3\n"
    for i in range (len(number_list)):
        if user == number_list[i]:
            if i == 6 or i == 3:
                number_list[i] = "x\n"
            else:
                number_list[i] = "x"


def outcome_o(number_list, o_games):

    for i in range (len(number_list)):

        if number_list[1] == "o" and number_list[2] == "o" and number_list[3] == "o\n":
            print("\nPlayer o has won the game! Congratulations Player o!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif number_list[4] and number_list[5] and number_list[6] == "o" or "o\n":
            print("\nPlayer o has won a game!")
            o_games += 1
            number_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif number_list[7] and number_list[8] and number_list[9] == "o" or "o\n":
            print("\nPlayer o has won the game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif number_list[1] and number_list[4] and number_list[7] == "o" or "o\n":
            print("\nPlayer o has won the game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif number_list[2] and number_list[5] and number_list[8] == "o" or "o\n":
            print("\nPlayer o has won the game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif number_list[3] and number_list[6] and number_list[9] == "o" or "o\n":
            print("\nPlayer o has won the game!")
            o_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif number_list[1] and number_list[5] and number_list[9] == "o" or "o\n":
            print("\nPlayer o has won the game!")
            o_games += 1
            number_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        elif number_list[3] and number_list[5] and number_list[7] == "o" or "o\n":
            print("\nPlayer o has won the game!")
            o_games += 1
            number_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return o_games

        else:
            pass

# finding the outcome for the player using x
def outcome_x(number_list, x_games):
    for i in range (len(number_list)):
        if number_list[1] and number_list[2] and number_list[3] == "x" or "x\n":
            print("\nPlayer x has won the game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif number_list[4] and number_list[5] and number_list[6] == "x" or "x\n":
            print("\nPlayer x has won the game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif number_list[7] and number_list[8] and number_list[9] == "x" or "x\n":
            print("\nPlayer x has won the game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif number_list[1] and number_list[4] and number_list[7] == "x" or "x\n":
            print("\nPlayer x has won the game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif number_list[2] and number_list[5] and number_list[8] == "x" or "x\n":
            print("\nPlayer x has won the game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif number_list[3] and number_list[6] and number_list[9] == "x" or "x\n":
            print("\nPlayer x has won the game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif number_list[1] and number_list[5] and number_list[9] == "x" or "x\n":
            print("\nPlayer x has won the game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        elif number_list[3] and number_list[5] and number_list[7] == "x" or "x\n":
            print("\nPlayer x has won the game!")
            x_games += 1
            num_list = ["", "1", "2", "3\n", "4", "5", "6\n", "7", "8", "9"]
            return x_games

        else:
            pass

#tic tac toe 
#Zanna Johnson

if __name__ == "__main__":
    main() 
