# Write your code here 👇

for i in range(1, 101):
    if i % 3 != 0:
        if i % 5 != 0:
            print(i)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    if i % 5 == 0 and i % 3 != 0:
        print("Buzz")
