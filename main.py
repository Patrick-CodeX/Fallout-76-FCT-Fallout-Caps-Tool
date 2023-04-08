import pandas as pd
import csv


def Fallout_Weapon(Weapon):
# Function that finds what weapon you're talking about.
    with open('Fallout76.csv', encoding="utf8") as csvfile:
    # Opens CSV File.
        csv_file = csv.reader(csvfile)
        #Reads CSV File.
        for row in csv_file:
        #Finds the Weapon by going through each row and Column in the CSV file.
            if Weapon.upper() in row[0].upper() or row[0].lower().startswith(Weapon.lower()):
                return row[0]

# Creates a Dataframe of the CSV File.
df = pd.read_csv('Fallout76.csv')

print(df)
# Takes the name of the weapon.
Name = input("Input the Name of the Weapon. ")


print('\n')
# Searches through the CSV file.
Weapon = Fallout_Weapon(Name)
# If the variable Weapon has a value print out the Weapon.
if Weapon:

    print("The Weapon you've chosen is", Weapon)
