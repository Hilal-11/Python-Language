import random 
# VARIABLES

# def get_choices() :
#     players_choice = "rock"
#     computer_choice = "paper"
#     return player_choice

# def  greeting() :
#     return "Hello Everyone"

# response = greeting()
# print(response)


# def get_choices() :
#     player_choice = "rock"
#     computer_choice = "paper"
    
#     return player_choice

# choices = get_choices()
# print(choices)


# Discteniories
# age = 22
# dict = {
#     "name": "Hilal" ,
#     "color" : "white",
#     "address" : "Kupwara",
#     "age" : age
    
#     }
# print(dict)


# def get_choices() :
#     player_choice = input("Enter a choice (rock , paper , scissor) :- ")
#     options = ["rock" , "paper" , "scessiors"]
#     computer_choice = random.choice(options)
#     choice = {"player" : player_choice , "computer" : computer_choice}
#     return choice

# choices = get_choices()
# print(choices)

    # lists in python
# food = ["A" , "B" , "C"]
# print(food)


# colors = ["red" , "green" , "orange" , "blue" , "royalblue"]
# getColor = random.choice(colors)
# print(getColor)


def get_choices() :
    player_choice = input("Enter a choice (rock , paper , scissor) :- ")
    options = ["rock" , "paper" , "scessiors"]
    computer_choice = random.choice(options)
    choice = {"player" : player_choice , "computer" : computer_choice}
    return choice



def check_win(player , computer) :
    # print("you choose "+player + " computer choose " + computer)
    # print("you choose ",player , " computer choose " , computer)
    print(f"you choose {player} , computer choose {computer}")
    if player == computer :
        print("it's a tie")
    elif player == "rock" and computer == "scessiors" :
        print("Rock smaashes scessiors ! You win")
    elif player == "rock" and computer == "paper" :
        print("Papers covers rock ! you lose.")
    else :
        print("Not tie !!!")

check_win("rock" , "scessiors")