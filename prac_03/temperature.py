"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(inputx("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Celsius: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} F".format(celsius))
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")