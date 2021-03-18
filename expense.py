#Author: Paul Knuckey
#Project: Bill Calculator
#Date: March 3, 2021
#An simple blil calculator, I know people who strugle with this.
#Done to work on my pyhon skills as I am way out of practice
#Will update as time goes on



print("Monthly Bill Calualtor")
print("If no payment is required enter 0")
print("")
#This is done through most of the app several times
#it's all the same
#collect ammont, convert string to float
pay = input("How much did you get paid? $")
pay = float(pay)
#test the conversion took
#print(type(pay))

day_care = input("Day Care Payment: $")
day_care = float(day_care)
#input(type(day_care))

house = input("House Payment: $")
house = float(house)
#print(type(house))

web = input("Internet Payment: $")
web = float(web)
#print(type(web))

hulu = input("Hulu Payment: $")
hulu = float(hulu)
#print(type(hulu))

xm = input("Xm Radio payment: $")
xm = float(xm)
#print(type(xm))
car = input("Car Payment: $")
car = float(car)
#print(type(car))

netflix = input("Netflix Payment: $")
netflix = float(netflix)
#print(type(netflix))

cameo = input("Cameo Payment: $")
cameo = float(cameo)
#print(type(cameo))
ny_life = input("NY life Insurance payment: $")
ny_life = float(ny_life)
#print (type(ny_life))

health = input("Health Payment: $")
health = float(health)
#print(type(health))

car_insure = input("Car Insurance payment: $")
car_insure = float(car_insure)
#print(type(car_insure))

massage = input("Massage Envy Payment: $")
massage = float(massage)
#print(type(massage))

water = input("Water Payment: $")
water = float(water)

#print(type(water))
gas = input("gas payment: $")
gas = float(gas)
#print(type(gas))

unplan = input("Unplaned expenses: $")
unplan = float(unplan)
#print(type(unplan))

#Calculations performed and inserted in expence varitable
expense = day_care + house + web + hulu + xm + car + netflix + cameo + ny_life + health + car_insure + massage + water + gas + unplan
expense = float(expense)

#limit output to 2 decimel places
expense = "{:.2f}".format(expense)

#use f formating to print out expences
print(f"Total payment for values entered: ${expense}")
expense = float(expense)

#Money left after expenses
print(type(pay))
print(type(expense))
left_pay = float(pay - expense)


#space and ouptut money left
print("")
left_pay = "{:.2f}".format(left_pay)
print(f"Money after expenses ${left_pay}")

