"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()


    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fah2 = cal_fah(celsius)
            print("Result: {:.2f} F".format(fah2))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            cel2 = cal_cel(fahrenheit)
            print("Result: {:.2f} F".format(cel2))
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()




