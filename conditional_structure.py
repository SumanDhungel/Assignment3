
#Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit,
# the program instructs to release the fish back into the lake
# and notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.
zander = int(input("Enter the length in cm: "))
if zander >= 42:
    print("the length is fulfilled")
else:
    req= 42 - zander
    print(f"release the fish back to the lake, it is {req} cm below size limit.")

'''
#Write a program that asks the user to enter the cabin class of a cruise ship and
# then prints out a written description according to the list below.
# You must use an if/elif/else structure in your solution.
#LUX: upper-deck cabin with a balcony.
#A: above the car deck, equipped with a window.
#B: windowless cabin above the car deck.
#C: windowless cabin below the car deck.
#If the user enters an invalid cabin class,
# the program outputs an error message Invalid cabin class.
cabin_class = input("Enter the cabin class (LUX/A/B/C): ")
if cabin_class == "LUX":
    print("upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("above the car deck, equipped with a window")
elif cabin_class == "B":
    print("windowless cabin above the car deck")
elif cabin_class == "C":
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class")
'''
'''
#Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
#A normal hemoglobin value for adult females is between 117-155 g/l.
#A normal hemoglobin value for adult males is between 134-167 g/l.

gender = input("Enter your gender (M/F): ")
hemoglobin = float(input("Enter your hemoglobin (g/l): "))
if gender == "M" and 134 <= hemoglobin <= 167:
    print("The hemoglobin is normal")
elif gender == "M" and hemoglobin > 167:
        print("The hemoglobin value is high")
elif gender == "M" and hemoglobin < 134:
        print("The hemoglobin value is low")
if gender == "F" and 117<= hemoglobin <= 155:
    print("The hemoglobin is normal")
elif gender == "F" and hemoglobin > 155:
        print("The hemoglobin value is high")
elif gender == "F" and hemoglobin < 117:
        print("The hemoglobin value is low")
'''

'''
#Write a program that asks the user to enter a year and
# notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.
year =""
while year != "exit":
    year = int(input("Enter the year: "))
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        print("It is a leap year")
    else:
        print("It is not a leap year")
'''