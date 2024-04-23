row = int(input('Enter number of rows required: '))

for i in range(row):
    for j in range(row):
     print(' ', end='') 
    
    for j in range(2*i+1):
        if j==0 or j==2*i  :
            print('#',end='')
        else:
            print(' ', end='')
    print()
