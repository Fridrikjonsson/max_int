
#1, 2, 3, 6, 11, 20, 37, 68, 125, 230



n = int(input("Enter the length of the sequence: ")) # Do not change this line
num_1 = 0
num_2 = 0
num_3 = 1
sum = 0

for i in range (0, n):
    if i < 3:
        sum = num_2 + num_3
        print(sum)
        num_1 = num_2
        num_2 = num_3
        num_3 = sum
    
    else:
        sum = num_1 + num_2 + num_3
        print (sum)
        num_1 = num_2 
        num_2 = num_3
        num_3 = sum



