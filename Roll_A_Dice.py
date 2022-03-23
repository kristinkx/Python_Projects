# ***************** Roll A Dice Game *********************
# let's say we have a 12-sided dice :-).
# rules :
# sides 1 - 4: 5 pts;
# sides 6 and 12: 3 * side(number) pts;
# sides 7-9:  8 pts;
# side 5 : 10 pts
# side 10: 20 pts
# side 11: 11 pts
# each player rolls the dice 3 times and calculate the sum

import random
# set the lowest value and highest value of the dice
low_side = 1
high_side = 12

# get name input and greet the players
name1 = input("Player 1, Enter your name: ")
print("Hello " + name1 + '!' + ' Welcome to the fun Roll A Dice Game :-)')
name2 = input("Player 2, Enter your name: ")
print("Hello " + name2 + '!' + ' Welcome to the fun Roll A Dice Game :-)')

count = 3
score1 = 0
score2 = 0

# each player can roll the dice 3 times
for x in range(count):
    # each player rolls the dice
    p1_value = random.randint(low_side, high_side)
    p2_value = random.randint(low_side, high_side)

    # display the values
    print(name1 + ' got ' + str(p1_value))
    print(name2 + ' got ' + str(p2_value))

    # calculate total score 1
    if (p1_value >= 1) and p1_value <= 4:
        score1 += 5
    elif p1_value >= 7 and p1_value <= 9:
        score1 += 8
    elif p1_value == 5:
        score1 += 10
    elif p1_value == 10:
        score1 += 20
    elif p1_value == 11:
        score1 += 11
    elif p1_value == 6 or p1_value == 12:
        score1 += 3 * p1_value

    # calculate total score 2
    if (p2_value >= 1) and p2_value <= 4:
        score2 += 5
    elif p2_value >= 7 and p2_value <= 9:
        score2 += 8
    elif p2_value == 5:
        score2 += 10
    elif p2_value == 10:
        score2 += 20
    elif p2_value == 11:
        score2 += 11
    elif p2_value == 6 or p2_value == 12:
        score2 += 3 * p2_value

    if score1 > score2:
        print(name1 + ' ' + 'won this round.')
    elif score1 < score2:
        print(name2 + ' ' + 'won this round.')
    elif score1 == score2:
        print("It's a tie")

    # roll again?
    roll_again = input('Roll again? Press Y/y/Enter to roll, N/n to quit: ')
    if roll_again in ['yes', 'Yes', 'Y', 'y', 'YES']:
        # do nothing
        pass
    elif roll_again in ['no', 'No', 'N', 'n', 'NO']:
        print(name1 + ', ' + "See you Next time!")
        print(name2 + ', ' + "See you Next time!")
        break
    else:
        print("You didn't give an answer. Roll again?")

# display the winner
print(name1 + ' total score =', score1)
print(name2 + ' total score =', score2)
if score1 > score2:
    print('Winner:', name1)
elif score1 < score2:
    print('Winner:', name2)
elif score1 == score2:
    print("It's a tie!")
