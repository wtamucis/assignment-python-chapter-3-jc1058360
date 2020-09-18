# Follow the assignment instructions to code an app that
# will tell a user their birthstone.
print("What is your birthstone?")
user_input = ""
user_input = input("Enter the number of the month you were born (1-12) >")
month = int(user_input)
message = "Your birthstone is"
if month == 1:
    print(f"{message} garnet.")

elif month == 2:
    print(f"{message} amethyst.")

elif month == 3:
    print(f"{message} bloodstone.")

elif month == 4:
    print(f"{message} diamond.")

elif month == 5:
    print(f"{message} emerald.")

elif month == 6:
    print(f"{message} pearl.")

elif month == 7:
    print(f"{message} ruby.")

elif month == 8:
    print(f"{message} peridot.")

elif month == 9:
    print(f"{message} sapphire.")

elif month == 10:
    print(f"{message} opal.")

elif month == 11:
    print(f"{message} topaz.")

elif month == 12:
    print(f"{message} turquoise.")
