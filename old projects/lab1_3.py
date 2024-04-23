#COUNT A DOLLAR GAME
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100
n_penny = input('enter the number of pennies: ')
n_nickel = input('enter the number of nickel: ')
n_dime = input('enter the number of dime: ')
n_quarter = input('enter the number of quarter: ')

total_penny = 1*int(n_penny)
total_nickel = 5*int(n_nickel)
total_dime = 10*int(n_dime)
total_quarter = 25*int(n_quarter)
total_cent = int(total_penny) + int(total_nickel) + int(total_dime) + int(total_quarter)
total_dollars = int(total_cent)/ int(PENNIES_IN_DOLLAR)
if int(total_dollars)> 1.0:
    print("sorry the amount you entered was more than a dollar")
elif int(total_dollars)<1.0:
    print("sorry the amount you entered was less than a dolar")
else:
    print("Congratulations!!! \n The amount you entered was exactly one dollar. \n You win the game!!")