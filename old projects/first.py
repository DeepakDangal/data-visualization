mydict = {
    "book":"kitab",
    "fan":"pankha",
    "love":"maya"
}

print("the english translation is:",mydict.keys())
a = input("enter a english word:")
print(f"The translation of the english word {a} is",mydict.get(a))


