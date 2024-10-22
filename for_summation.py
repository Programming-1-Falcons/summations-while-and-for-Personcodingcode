#for Summation code here
num = int(input("Enter number here :"))
x = 0
total = 0
for x in range(num + 1):
    print(x)
    total = total + x
    x = x + 1
print(total)
