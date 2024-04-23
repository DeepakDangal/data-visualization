year=[]
jan=float(input('Please enter Jan rainfall: '))
feb=float(input('Please enter Feb rainfall: '))
mar=float(input('Please enter Mar rainfall: '))
apr=float(input('Please enter Apr rainfall: '))
may=float(input('Please enter May rainfall: '))
jun=float(input('Please enter Jun rainfall: '))
jul=float(input('Please enter Jul rainfall: '))
aug=float(input('Please enter Aug rainfall: '))
sep=float(input('Please enter Sep rainfall: '))
oct=float(input('Please enter Oct rainfall: '))
nov=float(input('Please enter Nov rainfall: '))
dec=float(input('Please enter Dec rainfall: '))
year.extend((jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec))

def lowest():
    print('The minimum rainfall is', min(year))
lowest()

def highest():
    print('The most rainfall is', max(year))
highest()

def total():
    print('The total rainfall is', sum(year))
total()

def average():
    print('The average rainfall is', float(sum(year))/len(year))
average()


