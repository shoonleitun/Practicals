def main():

    item_no = int(input("Number of item: "))
    total = 0
    while item_no <= 0:
        print("Invalid number of items.")
        item_no = int(input("Number of item: "))

    for i in range(item_no):
        price = float(input("Price of item: "))
        total += price

    if total >= 100:
            total = total * 0.9

    print("Total price for {} is $ {}".format(item_no, total))

main()