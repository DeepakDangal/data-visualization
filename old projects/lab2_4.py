cart = {}
count = 0
Maximum_price = 5
print("WELCOME TO THE AMANDO SHOPPING SITE")
print("A: Add product to the cart.")
print("B: Search the product.")
print("C: Delete the product from the cart.")
print("D: Quit.")
while True: 
  choice = input("Enter your choice: ")
  if choice == "1":
    no_Items = int(input("Enter the number of items to be added in the shop: "))

    for i in range(0, no_Items):
      if count == Maximum_price:
        print("Cart is full.")
      else:
        product = input("Enter the product name: ")
        brand = input("Enter the brand name: ")
          
        cart[product] = brand
          
        count += 1
    print("You have added following items to the cart:")    
    for a,b in cart.items():
      print(f"{a} : {b}")
  
  elif choice == "2":
      product = input("Enter the items to be searched: ")
      
      if product in cart:
          print(f"{product}: {cart[product]}")
      else:
          print("No product exists with this name.")

  elif choice == "3":
      product = input("Enter the item to be deleted: ")
      
      if product in cart:
        del cart[product]
          
        count -= 1
          
        print("Product deleted from the cart.")
          
      elif count == 0:
        print("This Cart is empty, no item is found.")
      else:
        print(" There is no product exists with this name.")
  
  elif choice == "4":
      print("Thank you!")
      break
    
  else:
      print(" You have entered the Wrong Option!")
