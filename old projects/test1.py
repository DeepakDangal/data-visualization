primary_color1 = input('Enter the primary colors in lower case: ')
primary_color2 = input('Enter the second primary color in lower case: ')

if (primary_color1 == "red" and primary_color2 == "blue") or (primary_color1 == "blue" and primary_color2 == "red"):
    print( " purple")
elif (primary_color1 == "red" and primary_color2 == "yellow") or (primary_color1 == "yellow" and primary_color2 == "red"):
    print( "orange")
elif (primary_color1 == "blue" and primary_color2 == "yellow") or (primary_color1 == "yellow" and primary_color2 == "blue"):
    print( "green")
else:
    print("Error occured")
