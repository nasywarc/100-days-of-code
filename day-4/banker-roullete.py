# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
tot_person = len(names)
whos_gonna_pay = random.randint(0, (tot_person - 1))
print (names[whos_gonna_pay] + " " + "is going to buy the meal today!")
