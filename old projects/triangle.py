import random
def gamewin(comp,you):
	if comp==you:
		return None
	elif comp=="s":
		if you=="w":
			return False
			if you=="g":
				return True
	elif comp=="w":
		if you=="g":
			return False
			if you=="s":
				return True
	elif comp=="g":
		if you=="s":
			return False
			if you=="w":
				return True
	
print("comp turn: snake(s) water(w) gun(g)?:")
random_no=random.randint(1,3)

if random_no==1:
	comp="s"
elif random_no==2:
	comp="w"
elif random_no==3:
	comp="g"

you=input("your turn:snake(s) water(w) gun(g)?:")
a = gamewin(comp,you)
print(f"computer choose {comp}")
print(f"you choose {you}")

if a==None:
	print("this game is tie")
elif a:
	print("you win!")

else:
	print("you loose!!")



