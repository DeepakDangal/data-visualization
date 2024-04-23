print("WELCOME TO THE THE GRANN'S PHONE DIRECTORY MENU ")
phone_directory={}
z=0
while z==0:
  print("Menu")
  print("1 : Add a record")
  print("2 : Search a record")
  print("3 : Update a record")
  print("4 : Delete a record")
  print("5 : Quit")
  x=int(input("enter your choice : "))
  if(x==1):
    name=input(str("Enter your name : "))
    number=input(str("Enter your 10-digit phone number : "))
    phone_directory[name]=number
    print("Record added")
  elif(x==2):
    name=input("Enter your name : ")
    for key in phone_directory:
      if key==name:
        
        print(name+" : "+phone_directory[name]+"\n")
     
  elif(x==3):
    name=input("Enter your name : ")
    for key in phone_directory:
      if key==name:
        num=input(str("Enter new 10-digit phone number : "))
        phone_directory[name]=num
        print("updated \n")
      
  elif(x==4):
    name=str(input("Enter your name : "))
    for key in phone_directory.copy():
      if key==name:
        phone_directory.pop(name)
        print("record deleted"+"\n")
  elif(x==5):
    z=1
    z+=0