#Finna ut hvernig thetta virkar
#1, 2, 3, 6, 11, 20, 37, 68, 125, 230
#
n = int(input("Enter the length of the sequence: ")) # Do not change this line
num_1 = 1
num_2 = 2
num_3 = 3
count = 0
for i in range (0, n):
    num_4 = num_1 + num_2 + num_3
    num_5 = num_2 + num_3 + num_4
    count += i
    print (n)


