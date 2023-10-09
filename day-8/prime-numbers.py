# Write your code below this line 👇
def prime_checker(number):
    divider = 0
    for i in range(47):
        if number % (i+1) == 0:
            divider += 1
    if divider <= 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
