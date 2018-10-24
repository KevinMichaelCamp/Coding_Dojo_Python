#For Loop Basic 1

# 1. - Print all the numbers/integers from 0 to 150
for num in range(0, 151):
    print(num)

# 2. - Print all the multiples of 5 from 5 to 1,000,000
for five in range(0,100001):
    if(five % 5 == 0):
        print(five)

## 3. - Print integers 1 to 100. If divisible by 5, print 'Coding', if divisible by 10 "Coding Dojo"
for num in range(1, 101):
    if(num % 10 == 0):
        print("Coding Dojo")
    elif(num % 5 == 0):
        print("Coding")
    else:
        print(num)

# 4. - Add odd integers from 0 to 500,000, and print the final sum
sum = 0

for num in range(0, 50):

    if(num % 2 != 0):
        sum = sum + num
        print(sum)

print("FINAL SUM: ", sum)

# 5. - Print positive numbers starting at 2018, couting down by fours(exclude 0)
for num in range(2018, 0, -1):
    if(num % 4 == 0):
        print(num)

# 6. - Given 'lolwNum', 'highNum', 'mult', print multiples of mult from lowNum to highNum, using a FOR loop. For (2,9,3), print 3 6 9 (on succesive lines)
def multiples(lowNum, highNum, mult):
    for num in range(lowNum, highNum):
        if(num % mult == 0):
            print(num)



# Test Case
multiples(0,100,2)
multiples(0,100,3)
multiples(0,100,4)
