#Author: Paul Knuckey
#Project: Bill Calculator
#Date: March 19, 2021
#An simple blil calculator, I know people who strugle with this.
#Done to work on my pyhon skills as I am way out of practice
#Will update as time goes on



print("Monthly Bill Calualtor")
#print("If no payment is required enter 0") 
print("")
#This is done through most of the app several times
#it's all the same
#collect ammont, convert string to float if no value is entered zero will be returned
pay = float(input("How much did you get paid? $") or "0")
#test the conversion took
#print(type(pay))

day_care = float(input("Day Care Payment: $") or "0")
#input(type(day_care))

house = float(input("House Payment: $") or "0")
#print(type(house))

web = float(input("Internet Payment: $") or "0")
#print(type(web))

hulu = float(input("Hulu Payment: $") or "0")
#print(type(hulu))

xm = float(input("Xm Radio payment: $") or "0")
#print(type(xm))

car = float(input("Car Payment: $") or "0")
#print(type(car))

netflix = float(input("Netflix Payment: $") or "0")
#print(type(netflix))

cameo = float(input("Cameo Payment: $") or "0")
#print(type(cameo))

ny_life = float(input("NY Life Insurance payment: $") or "0")
#print (type(ny_life))

health = float(input("Health Payment: $") or "0")
#print(type(health))

car_insure = float(input("Car Insurance payment: $") or "0")
#print(type(car_insure))

massage = float(input("Massage Envy Payment: $") or "0")
#print(type(massage))

water = float(input("Water Payment: $") or "0")
#print(type(water))

gas = float(input("Gas payment: $") or "0")
#print(type(gas))

fuel = float(input("Fuel Cost: $") or "0")
#print(type(fuel))

phone = float(input("Phone Bill: $") or "0")
#print(type(phone))

grocery = float(input("Grocery cost: $") or "0")
#print(type(grocery))

unplan = float(input("Unplaned Expenses: $") or "0")
#print(type(unplan))

#Calculations performed and inserted in expence varitable
expense = float(day_care + house + web + hulu + xm + car + netflix + cameo + ny_life + health + car_insure + massage + water + gas + fuel + phone+ grocery + unplan)

#limit output to 2 decimel places
expense = "{:.2f}".format(expense)

#use f formating to print out expences
print(f"Total payment for values entered: ${expense}")
expense = float(expense)

#Money left after expenses
left_pay = float(pay - expense)


#space and ouptut money left
print("")
left_pay = "{:.2f}".format(left_pay)
print(f"Money after expenses ${left_pay}")
print("")
