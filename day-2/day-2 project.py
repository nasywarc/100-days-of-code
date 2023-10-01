#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
people = input("How many people to split the bill? ")
percent = input("What percentage tip would you like to give? 10, 12, or 15? ")

# merubah semua tipe data dari string ke float
total = float(total)
people = float(people)
percent = float(percent)

# melakukan perhitungan pajak dan total
tip = total*(percent/100)
to_pay = total + tip

# merubah tipe data ke float lagi
to_pay = float(to_pay)

# melakukan pentotalan harga
calc = to_pay/people
calc = float(calc)

# membatasi float sehingga hanya 1 angka di belakang koma
calc = round(calc, 2)

# mengubah tipe data calc agar bisa digabung dengan string di line 27
calc = str(calc)

print("Each person should pay: $" + calc)
