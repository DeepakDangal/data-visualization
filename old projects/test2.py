salary=float(input("Please enter your salary in Germany:"))
migrate=str(input("Enter the country you want to migrate to:"))

def convertSalary():
  
    eurcad = salary*1.36
    eurusd = salary*1.08
    eurpound = salary*0.83
    eurcambodian = salary*4,365.17

if migrate == "canada":
    if eurcad < 64000:
        print("You will be poor in Canada with a salary of" + float(eurcad), "cad")
else:
    print("You will be rich in Canada with a salary of" + float(eurcad) + "cad")

if migrate == "usa":

    if eurusd < 56516:
        print("You will be poor in Usa with a salary of" + float(eurusd) + "usd")
else:	
    print("You will be rich in Usa with a salary of" + float(eurusd) + "usd")

if migrate == " the uk":

    if eurpound < 35423:
        print("You will be poor in UK with a salary of" + float(eurpound) + "usd")
else:
    print("You will be rich in UK with a salary of" + float(eurpound) + "usd")		    

if migrate == "cambodia":

    if eurcambodian < 5649856:
        print("You will be poor in Cambodia with a salary of" + float(eurpound) + "Cambodian Riel")
else:
    print("You will be rich in Cambodia with a salary of" + float(eurpound) + "Cambodian Riel")
convertSalary()